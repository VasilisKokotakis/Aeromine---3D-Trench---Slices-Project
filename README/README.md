# Οδηγός Χρήσης - Trench Sections

 Σκοπός του Προγράμματος
Το πρόγραμμα αυτό χρησιμοποιείται για να αναλύσει point clouds (LAS αρχεία) και να δημιουργήσει τομές/sections κατά μήκος ενός άξονα.
Με αυτό τον τρόπο μπορούμε να μελετήσουμε εύκολα την κατανομή των σημείων και το ύψος τους.

Το αποτέλεσμα είναι:
- Ένα αρχείο Excel (CSV) με τα δεδομένα των τομών.
- (Προαιρετικά) Ένα γραφικό preview (HTML) για γρήγορη οπτική επιβεβαίωση.



 Εγκατάσταση

# Σε Debian / Ubuntu Linux
1. Βεβαιωθείτε ότι έχετε εγκατεστημένο το python3 και το pip:
 bash
 sudo apt update
 sudo apt install python3 python3-pip python3-venv -y
 
2. Δημιουργήστε και ενεργοποιήστε εικονικό περιβάλλον:
 bash
 python3 -m venv trench_env
 source trench_env/bin/activate
 
3. Εγκαταστήστε τα απαραίτητα πακέτα:
 bash
 pip install laspy pandas matplotlib
 

# Σε Windows
1. Κατεβάστε και εγκαταστήστε την πιο πρόσφατη έκδοση του Python από το [python.org](https://www.python.org/downloads/).
 - Κατά την εγκατάσταση τσεκάρετε την επιλογή “Add Python to PATH”.
2. Ανοίξτε το Command Prompt (cmd).
3. Δημιουργήστε εικονικό περιβάλλον:
 cmd
 python -m venv trench_env
 trench_env\Scripts\activate
 
4. Εγκαταστήστε τα πακέτα:
 cmd
 pip install laspy pandas matplotlib
 



 Χρήση

Για να τρέξετε το πρόγραμμα:

bash
python trench_sections.py --input <αρχείο.las> --auto-axis --spacing 0.10 --thickness 0.10 --decimate 100 --out sections.csv --preview




 Επεξήγηση των επιλογών (flags)

- --input <αρχείο.las>
Το αρχείο point cloud που θα αναλυθεί.

- --auto-axis
Αυτόματη επιλογή άξονα τομής (π.χ. κατά μήκος του μεγαλύτερου άξονα του cloud).

- --spacing <απόσταση>
Απόσταση μεταξύ των τομών (π.χ. 0.10 = ανά 10 εκατοστά).
👉 Μικρότερο spacing = περισσότερες τομές = μεγαλύτερη ακρίβεια αλλά πιο βαρύ.

- --thickness <πάχος>
Πάχος της κάθε τομής σε μέτρα (π.χ. 0.10 = 10 εκατοστά).

- --decimate <ποσοστό>
Μείωση του αριθμού σημείων για πιο γρήγορη επεξεργασία.
👉 Μεγαλύτερος αριθμός = λιγότερα σημεία (π.χ. 100 = κρατάει 1 στα 100 σημεία).

- --out <αρχείο.csv>
Όνομα αρχείου για αποθήκευση αποτελεσμάτων (μπορείτε να το ανοίξετε με Excel).

- --preview
Εμφάνιση γραφικής προεπισκόπησης των τομών (σε παράθυρο).



 Παραγόμενα Αρχεία

1. sections.csv → περιέχει τα δεδομένα των τομών (για άνοιγμα στο Excel).
2. sections_summary.csv → συνοπτικός πίνακας με πληροφορίες για κάθε τομή.
3. (Προαιρετικά) Παράθυρο προεπισκόπησης με γραφήματα.



 Συμβουλές

- Για μεγαλύτερη ακρίβεια → μειώστε το --spacing (π.χ. 0.05 αντί για 0.10).
- Για ταχύτερη εκτέλεση → αυξήστε το --decimate.
- Αν θέλετε μόνο το Excel χωρίς preview → μην βάλετε το flag --preview.
- Αν θέλετε μόνο γρήγορη οπτική επιβεβαίωση → κρατήστε το --preview αλλά δώστε μεγάλο --decimate (π.χ. 200).



 Παράδειγμα

bash
python trench_sections.py --input Skama_fusikou_aeriou_Point_Cloud.las --auto-axis --spacing 0.05 --thickness 0.10 --decimate 50 --out sections.csv --preview


👉 Αυτό θα δημιουργήσει το αρχείο sections.csv με υψηλή ακρίβεια (spacing 5cm) και θα ανοίξει προεπισκόπηση.
