import ipywidgets as widgets
from IPython.display import display, clear_output

# פונקציה ראשית להפעלת חדר הבריחה
def start_escape_room():
    clear_output()
    print("==========================================================")
    print("🔒 ברוכים הבאים לחדר הבריחה האינטראקטיבי: האקר בלב ים! 🔒")
    print("==========================================================")
    print("הספינה תקועה, ומערכות הניווט דורשות הגדרות רשת מדויקות כדי להשתחרר.")
    print("ענו על החידות בעזרת רכיבי המערכת שלפניכם.\n")
    
    show_riddle_1()

# --- 🎯 חידה 1: פורטים ---
def show_riddle_1():
    print("--- 🛰️ שלב 1: פרוטוקול HTTPS המאובטח ---")
    print("באיזה פורט (Port) משתמש הדפדפן כדי ליצור חיבור HTTPS מוצפן אל שרת הניווט?")
    
    port_dropdown = widgets.Dropdown(
        options=['בחר פורט...', '80', '22', '443', '53'],
        value='בחר פורט...',
        description='פורט:',
    )
    
    check_button1 = widgets.Button(
        description='בדיקת פורט',
        button_style='info',
        icon='key'
    )
    
    display(port_dropdown, check_button1)
    
    def on_click_1(b):
        if port_dropdown.value == '443':
            print("\n✅ תשובה נכונה! החיבור מאובטח והנעילה הראשונה נפתחה! 🔓\n")
            check_button1.disabled = True
            port_dropdown.disabled = True
            # מעבר אוטומטי לחידה 2
            show_riddle_2()
        elif port_dropdown.value == 'בחר פורט...':
            print("\n⚠️ אנא בחר פורט מתוך הרשימה!")
        else:
            print(f"\n❌ פורט {port_dropdown.value} חסום ב-Firewall של הספינה! נסה שוב.")
            
    check_button1.on_click(on_click_1)

# --- 🎯 חידה 2: חישוב רשתות (Subnetting) ---
def show_riddle_2():
    print("----------------------------------------------------------")
    print("--- 🗺️ שלב 2: ניתוב וחלוקת רשתות (Subnetting) ---")
    print("שרת הניווט קיבל את כתובת ה-IP הבאה: 192.168.10.45")
    print("מנהל הרשת הגדיר מסכת רשת (Subnet Mask) של: 255.255.255.0 (CIDR: /24)")
    print("מהי כתובת הרשת (Network ID) אליה שייך השרת?")
    print("----------------------------------------------------------")
    
    # תיבת טקסט להזנת הכתובת
    ip_input = widgets.Text(
        value='',
        placeholder='הקלד כתובת רשת (למשל: 10.0.0.0)',
        description='כתובת רשת:',
        disabled=False
    )
    
    check_button2 = widgets.Button(
        description='בדיקת כתובת רשת',
        button_style='warning', # כפתור כתום
        icon='network-wired'
    )
    
    display(ip_input, check_button2)
    
    def on_click_2(b):
        user_answer = ip_input.value.strip()
        if user_answer == "192.168.10.0":
            print("\n✅ מדהים! חישבתם את ה-Network ID במדויק! חצי מהדלת כבר פתוחה. ⚡\n")
            check_button2.disabled = True
            ip_input.disabled = True
            # כאן בשלב הבא נוסיף את חידה 3 (VLAN + סוכן AI)
        elif user_answer == "":
            print("\n⚠️ אל תשאיר את התיבה ריקה, המחשב מחכה לכתובת!")
        else:
            print(f"\n❌ הכתובת {user_answer} שגויה! הנתב לא מצליח למצוא את הרשת הזו. נסה שוב.")
            print("💡 רמז: במסכת /24, האוקטטה האחרונה (המספר האחרון) של הרשת תמיד מתאפסת.")
            
    check_button2.on_click(on_click_2)

# הפעלת המשחק
start_escape_room()
