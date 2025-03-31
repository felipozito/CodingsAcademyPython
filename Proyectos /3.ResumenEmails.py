import imaplib
import email
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from getpass import getpass
import ssl

# Descargar recursos necesarios de NLTK
# nltk.download('punkt')
# nltk.download('stopwords')

class EmailSummarizer:
    def __init__(self, email_user, email_pass):
        self.email_user = email_user
        self.email_pass = email_pass
        self.imap_server = "imap.gmail.com"
        self.context = ssl.create_default_context()
        
    def connect(self):
        """Conectar al servidor IMAP"""
        self.mail = imaplib.IMAP4_SSL(self.imap_server)
        self.mail.login(self.email_user, self.email_pass)
        self.mail.select('inbox')
    
    def summarize_text(self, text, num_sentences=3):
        """Generar resumen usando NLTK"""
        # Tokenizar y limpiar texto
        stop_words = set(stopwords.words('spanish'))
        words = word_tokenize(text.lower())
        words = [word for word in words if word.isalnum() and word not in stop_words]
        
        # Calcular frecuencia de palabras
        freq_dist = nltk.FreqDist(words)
        
        # Puntuar oraciones
        sentences = sent_tokenize(text)
        sentence_scores = {}
        
        for i, sentence in enumerate(sentences):
            for word in word_tokenize(sentence.lower()):
                if word in freq_dist:
                    if i in sentence_scores:
                        sentence_scores[i] += freq_dist[word]
                    else:
                        sentence_scores[i] = freq_dist[word]
        
        # Seleccionar las mejores oraciones
        top_sentences = sorted(sentence_scores, 
                             key=sentence_scores.get, 
                             reverse=True)[:num_sentences]
        
        return ' '.join([sentences[i] for i in sorted(top_sentences)])
    
    def process_emails(self, num_emails=5):
        """Procesar correos electrónicos"""
        try:
            _, data = self.mail.search(None, 'UNSEEN')
            email_ids = data[0].split()[-num_emails:]
            
            for e_id in email_ids:
                _, msg_data = self.mail.fetch(e_id, '(RFC822)')
                raw_email = msg_data[0][1]
                msg = email.message_from_bytes(raw_email)
                
                # Extraer contenido del correo
                subject = msg['subject']
                from_ = msg['from']
                body = ""
                
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            break
                else:
                    body = msg.get_payload(decode=True).decode()
                
                # Generar resumen
                summary = self.summarize_text(body)
                
                # Mostrar resultados
                print(f"\n{'='*50}")
                print(f"De: {from_}")
                print(f"Asunto: {subject}")
                print(f"\nResumen:\n{summary}")
                print(f"{'='*50}\n")
                
        except Exception as e:
            print(f"Error: {e}")
    
    def run(self):
        """Ejecutar el asistente"""
        self.connect()
        print("\nAsistente de resumen de correos electrónicos")
        while True:
            print("\nOpciones:")
            print("1. Ver resúmenes de correos no leídos")
            print("2. Salir")
            choice = input("Seleccione una opción: ")
            
            if choice == '1':
                num_emails = int(input("¿Cuántos correos quiere revisar? (max 10): "))
                self.process_emails(min(num_emails, 10))
            elif choice == '2':
                print("Saliendo...")
                break
            else:
                print("Opción inválida")

if __name__ == "__main__":
    user = input("Ingrese su email: ")
    password = getpass("Ingrese su contraseña: ")
    
    summarizer = EmailSummarizer(user, password)
    summarizer.run()