import sys
import math
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QComboBox, 
                             QLineEdit, QPushButton, QTableWidget, 
                             QTableWidgetItem, QVBoxLayout, QHBoxLayout, QHeaderView)

# ==========================================
# 1. DATASET SECTION
# ==========================================
# A sample database of influencers with categories, stats, and pricing
INFLUENCERS = [
    {"name": "TechWithAli", "category": "Tech", "followers": 500000, "engagement": 4.5, "cost": 1200},
    {"name": "MKBHD_Fan", "category": "Tech", "followers": 1200000, "engagement": 5.2, "cost": 3500},
    {"name": "Sara_Fits", "category": "Fitness", "followers": 300000, "engagement": 6.1, "cost": 800},
    {"name": "GymBro_Pro", "category": "Fitness", "followers": 850000, "engagement": 3.8, "cost": 2000},
    {"name": "Glam_by_Noor", "category": "Fashion", "followers": 450000, "engagement": 5.0, "cost": 1500},
    {"name": "Vogue_Vibes", "category": "Fashion", "followers": 150000, "engagement": 7.2, "cost": 600},
]

# ==========================================
# 2. SIMILARITY MATCHING LOGIC
# ==========================================
def calculate_match_score(brand_pref, influencer):
    # Filter out completely wrong categories first (Niche alignment constraint)
    if brand_pref["category"] != influencer["category"]:
        return 0.0
    
    # Normalize features to scale them uniformly between 0 and 1
    # This ensures large numbers (like followers) don't dominate the math
    target_f = brand_pref["followers"] / 2000000.0
    actual_f = influencer["followers"] / 2000000.0
    
    target_e = brand_pref["engagement"] / 10.0
    actual_e = influencer["engagement"] / 10.0
    
    target_c = brand_pref["budget"] / 5000.0
    actual_c = influencer["cost"] / 5000.0
    
    # Euclidean Distance Formula: sqrt( sum( (Target - Actual)^2 ) )
    distance = math.sqrt(
        (target_f - actual_f)**2 + 
        (target_e - actual_e)**2 + 
        (target_c - actual_c)**2
    )
    
    # Convert proximity distance into a similarity percentage
    similarity = max(0.0, 100.0 * (1.0 - distance))
    return round(similarity, 2)

def get_matches(brand_pref):
    results = []
    for inf in INFLUENCERS:
        score = calculate_match_score(brand_pref, inf)
        if score > 0:  # Only evaluate matching niches
            inf_result = inf.copy()
            inf_result["score"] = score
            results.append(inf_result)
            
    # Sort by highest similarity match profile down to the lowest
    return sorted(results, key=lambda x: x["score"], reverse=True)

# ==========================================
# 3. PYQT5 GRAPHICAL USER INTERFACE
# ==========================================
class InfluencerMatcherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Window configuration
        self.setWindowTitle('Muhammad Mehar Ali - Influencer Matcher')
        self.resize(700, 500)
        
        # Primary application layout layouts
        main_layout = QVBoxLayout()
        form_layout = QHBoxLayout()
        
        # --- Form Controls & Inputs ---
        self.cat_label = QLabel('Niche:')
        self.cat_input = QComboBox()
        self.cat_input.addItems(['Tech', 'Fitness', 'Fashion'])
        
        self.fol_label = QLabel('Followers Target:')
        self.fol_input = QLineEdit('500000')
        
        self.eng_label = QLabel('Engagement (%):')
        self.eng_input = QLineEdit('5.0')
        
        self.bud_label = QLabel('Budget ($):')
        self.bud_input = QLineEdit('1500')
        
        self.match_btn = QPushButton('Find Best Matches')
        # Setup application Signal handling link to Slot execution context
        self.match_btn.clicked.connect(self.run_matching)
        
        # Assemble input controls line structural frame
        form_layout.addWidget(self.cat_label)
        form_layout.addWidget(self.cat_input)
        form_layout.addWidget(self.fol_label)
        form_layout.addWidget(self.fol_input)
        form_layout.addWidget(self.eng_label)
        form_layout.addWidget(self.eng_input)
        form_layout.addWidget(self.bud_label)
        form_layout.addWidget(self.bud_input)
        
        # --- Structured Table Data View Component ---
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Name', 'Followers', 'Engagement Rate', 'Campaign Cost', 'Match Score'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Layer layout hierarchies directly down to parent canvas frame
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.match_btn)
        main_layout.addWidget(self.table)
        
        self.setLayout(main_layout)
        
    def run_matching(self):
        # Parse visual configurations from explicit UI bindings into dictionary parameters
        try:
            brand_preferences = {
                "category": self.cat_input.currentText(),
                "followers": float(self.fol_input.text()),
                "engagement": float(self.eng_input.text()),
                "budget": float(self.bud_input.text())
            }
        except ValueError:
            # Simple handling logic to prevent crash errors if text fields are empty/invalid
            return

        # Perform similarity mathematical evaluation iterations
        matched_influencers = get_matches(brand_preferences)
        
        # Clear past rows and populate refreshed calculated targets
        self.table.setRowCount(0)
        for row_idx, inf in enumerate(matched_influencers):
            self.table.insertRow(row_idx)
            self.table.setItem(row_idx, 0, QTableWidgetItem(inf["name"]))
            self.table.setItem(row_idx, 1, QTableWidgetItem(f"{inf['followers']:,}"))
            self.table.setItem(row_idx, 2, QTableWidgetItem(f"{inf['engagement']}%"))
            self.table.setItem(row_idx, 3, QTableWidgetItem(f"${inf['cost']}"))
            self.table.setItem(row_idx, 4, QTableWidgetItem(f"{inf['score']}%"))

# ==========================================
# 4. EXECUTION POINT
# ==========================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InfluencerMatcherApp()
    ex.show()
    sys.exit(app.exec_())