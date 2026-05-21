import ipywidgets as widgets
from IPython.display import display, clear_output

# פונקציה שמנקה את המסך ומציגה את החידה הראשונה
def start_escape_room():
    clear_output()
    print("==========================================================")
    print("🔒 ברוכים הבאים לחדר הבריחה האינטראקטיבי: האקר בלב ים! 🔒")
    print("==========================================================")
    print("נוסעי הספינה מנסים לגלוש לאתרים מאובטחים, ועליכם לוודא שהרשת תקינה.")
    print("הדלת תפתח רק אם תענו נכון על החידות בעזרת רכיבי המערכת.\n")
    
    # חידה 1: פורטים
    print("--- 🎯 חידה 1: פרוטוקול HTTPS המאובטח ---")
    print("באיזה פורט (Port) משתמש הדפדפן כדי ליצור חיבור HTTPS מוצפן אל שרת האינטרנט?")
    
    # יצירת תפריט בחירה (Dropdown) לתלמידים
    port_dropdown = widgets.Dropdown(
        options=['בחר פורט...', '80', '22', '443', '53'],
        value='בחר פורט...',
        description='פורט:',
        disabled=False,
    )
    
    # כפתור בדיקה
    check_button = widgets.Button(
        description='בדיקת תשובה',
        button_style='info', # כפתור כחול
        tooltip='לחץ כאן לבדיקת הפורט',
        icon='key'
    )
    
    # הצגת הרכיבים על המסך
    display(port_dropdown, check_button)
    
    # מה קורה כשהתלמיד לוחץ על הכפתור
    def on_button_clicked(b):
        if port_dropdown.value == '443':
            print("\n✅ תשובה נכונה! המעטפת הוצפנה בהצלחה, ונפתחה הנעילה הראשונה! 🔑")
            check_button.disabled = True
            port_dropdown.disabled = True
            # כאן נעבור בהמשך לחידה 2
        elif port_dropdown.value == 'בחר פורט...':
            print("\n⚠️ אנא בחר פורט מתוך הרשימה!")
        else:
            print(f"\n❌ פורט {port_dropdown.value} אינו נכון! השרת חסם את הגישה. נסה שוב.")
            
    check_button.on_click(on_button_clicked)

# הפעלת המשחק
start_escape_room()
