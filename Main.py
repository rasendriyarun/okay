import streamlit as st

def intro():
    import streamlit as st

    st.title("Hello! Verify yourself first.")

    st.markdown("Are you RAFLI NUR MUHAMAD?")
    # Pastikan session_state.clicked sudah ada sebelum digunakan
    if "clicked" not in st.session_state:
        st.session_state.clicked = None

    # Design button
    st.markdown(
        """
        <style>
            div.stButton > button {
                font-size: 18px;
                font-weight: bold;
                padding: 10px 24px;
                border-radius: 10px;
                border: none;
                cursor: pointer;
                transition: 0.3s;
                width: 130px;
            }
            div.stButton > button:first-child {
                background-color: white !important; /* Warna putih */
                color: black;
            }
            div.stButton > button:first-child:hover {
                background-color: #dbd9d9 !important; /* Abu-abu saat hover */
            }
            div.stButton > button:last-child {
                background-color: white !important; /* Warna merah */
                color: black;
            }
            div.stButton > button:last-child:hover {
                background-color:#dbd9d9 !important; /* Abu-abu saat hover */
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Membuat tombol YES dan NO dalam satu baris
    col1, col2, col3 = st.columns([1, 2, 1])  # Posisikan tombol di tengah
    with col2:
        col_yes, col_no = st.columns(2)
        with col_yes:
            if st.button("YEA", key="yes"):
                st.session_state.clicked = "yes"
        with col_no:
            if st.button("HMM YEA", key="no"):
                st.session_state.clicked = "no"
    
    st.markdown("       ")

    # Jika tombol sudah ditekan, tampilkan teks & gambar
    if st.session_state.clicked == "yes":
        col1, col2, col3 = st.columns([0.2, 4, 0.2])
        with col2:
            st.markdown(
                """
            <div style="
                border: 10px solid grey;  
                padding: 25px; 
                border-radius: 10px; 
                background-color: white; 
                color: black; 
                text-align: center; 
                max-width: 3200px; 
                margin: auto;
                box-shadow: 5px 5px 15px rgba(0.2, 0, 0, 0.2);  
            ">
                <h3 style="text-align: center;">Happy happiest birthday rrrafli🐨!</h2>
                <p style="text-align: justify;">
                    Kamu pasti bingung kan ini apaa HAHAHAH. Haappy birthdaaay yah!!! Aku ngga kasih wishnya disini, abis kamu baca ini, 
                    kamu langsung klik side panel yg wishes okay?😉 Kalo kuenya uda kemaren yaah hihi, MAAF KALO AGAK KACAU YA TAPI 😢
                </p>
            </div
            <p>
                        
            </p>
            <p style="text-align: center;">
                    I'll drop it here biar kamu ngga lupa bentukan masterpiece mini cake naruto merem n happy ini heheheh😏
                </p>
            """, 
                unsafe_allow_html=True
            )
        # Gambar kue
        col1, col2, col3 = st.columns([1.1, 3, 1])
        with col2:
            st.image("cake.jpg", width=500)

    elif st.session_state.clicked == "no":
        col1, col2, col3 = st.columns([0.5, 2, 0.5])
        with col2:
            st.markdown(
                """
                <div style="
                    border: 8px solid maroon;  
                    padding: 20px; 
                    border-radius: 0px; 
                    background-color: maroon;  
                    color: white;  
                    text-align: center;  
                    max-width: 1200px; 
                    margin: auto;
                    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);  
                ">
                    <h2>KOK PAKE HMM?? KAMU BUKAN RAFLI? 😠</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

def wishes():
    import streamlit as st
    import pandas as pd

    st.title("Happy birthday!")

    st.markdown(
        """
        <div style="
            border: 35px solid white;  
            padding: 20x; 
            border-radius: 0px; 
            background-color: white; 
            color: black; 
            text-align: center; 
            max-width: 3500px; 
            margin: auto;
            box-shadow: 5px 5px 15px rgba(0.2, 0, 0, 0.2);  
        ">
            <p style="text-align: justify;">
                OMG can't believe this is the third time we celebrate your birthday together??? I have pretty much thing to say sih for this year's birthday. Pertamaa of course, I wish you alllll the good things this world could ever give. I also wish you tons of happiness, always always always. 
                Take a good care of your health ya! Kita ngga tau habis ini kita bakal melanjutkan hidup dimana hahah, and kalo ngga si surabaya, you only have yourself there. Soo, be healthy terusss! Kasihan bapak ibuk sedih kalo kamu sakitt. Makin sayang and nurut sama bapak ibuk yaah.
                </p>
            <p style="text-align: justify;">
                Tahun lalu and tahun sebelumnya aku kasih wish masih bisa nyebut semester ya, sekarang udah ngga bisa nyebut semester loh🙂 time do flies too fast yaah🙂 Semoga dilancarin semua urusan kamu yaa dari wisuda, apply kerja, sampe nanti kamu uda menjalani battle yang sesungguhnya (kerjaa). 
                You always have my support in eeeverything you do, always have and always will. No one knows di depan bakalan ada problems apa yang uda nungguin kita, so I hope you can overcome it well yaaa. Semoga masalah-masalah yang nantinya bakal kamu hadapin bisa kamu selesein semuanyaa. 
                </p>
            <p style="text-align: justify;">
                If you’re struggling about something (someday) don’t ever hesitate to share it with me ya! Im all ears kalo kamu mau cerita tentang apapun, aku juga bakal bantu kamu find a way out kalo nantinya kamu lagi ada masalah. Jangan pernah mikir-mikir juga ya kalo mau share your worries ke aku. 
                I will always let you borrow my shoulders if you need something to lean on to😁👍🏻 and also a hug🤗
                </p>
            <p style="text-align: justify;">
                Terakhir, aku mau minta maaf buat kesalahanku kemaren ya. I was being too hard and mean to you. I am truly sorry. Maaf yaa aku masih belum bisa ngambil keputusan dengan baik dan bijak…. Okay ini beneran last banget, once again happy birthday ya rafli. I hope all your wishes will slowly come true yaaa. 
                Keep being the kind-hearted rafli like you’ve always been okkkaayy😊🖤 
                </p>
        </div>
        """,
        unsafe_allow_html=True
    )

def gifts():
    import streamlit as st
    import time
    import numpy as np

    # Inisialisasi session state jika belum ada
    if "selected_gift" not in st.session_state:
        st.session_state.selected_gift = None
        
    st.markdown(
    """
    <div style="
            border: 0px solid white;  
            padding: 10x; 
            border-radius: 10px; 
            background: linear-gradient(to bottom, #6c7487, white);  /* Gradasi dari grey ke white */ 
            color: navy; 
            text-align: center; 
            max-width: 8000px; 
            margin: auto;
            box-shadow: 5px 5px 15px rgba(0.2, 0, 0, 0.2);  
        ">
    <h1 style="text-align: center; color: black;">🌟 Welcome to the gift shop! 🌟</h1>
    """,
    unsafe_allow_html=True
)
    st.markdown("  ")
    # Gambar gift shop
    col1, col2, col3 = st.columns([0.4, 3, 0.4])
    with col2:
        st.image("giftshop.jpg", width=1200)

    st.markdown(
        """
        <h4 style="text-align: center;">What kind of gift you choose to unveil?</h4>
        """,
        unsafe_allow_html=True
    )
    # Styling tombol dengan CSS
    st.markdown(
        """
        <style>
            .stButton > button {
                background-color: #75839e; /* Warna grey */
                color: black; /* Warna teks hitam */
                font-size: 18px;
                font-weight: bold;
                padding: 15px 25px;
                border-radius: 10px;
                border: none;
                cursor: pointer;
                transition: 0.3s;
            }
            .stButton > button:hover {
                background-color: #ccd6eb; /* Warna abu-abu muda saat hover */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Menggunakan kolom agar tombol berada di tengah
    col1, col2, col3 = st.columns([0.5, 2, 0.5])

    with col2:  # Semua tombol ada di kolom tengah agar sejajar dengan teks
        btn_col1, btn_col2, btn_col3 = st.columns(3)
        
        with btn_col1:
            if st.button("T-SHIRT"):
                st.session_state.selected_gift = "T-SHIRT"
                
        with btn_col2:
            if st.button("PERFUME"):
                st.session_state.selected_gift = "PERFUME"

        with btn_col3:
            if st.button("HEALTH KIT"):
                st.session_state.selected_gift = "HEALTH KIT"

    # Menampilkan teks sesuai dengan tombol yang diklik
    if st.session_state.selected_gift == "T-SHIRT":
        st.markdown(
            """
            <div style="border-radius: 10px; padding: 20px; background: linear-gradient(to bottom, #d6d4d4, white); color: black; text-align: justify;">
                <div style="border-radius: 5px; padding: 20px; background: linear-gradient(to bottom, #d6d4d4, white); color: black; text-align: justify;">
                <p>Kalo t-shirt ini JUJUR reason number 1 aku kadoin kamu ini karena aku sukaa banget kamu pake kaos warna grey (aku perna bilang ke kamu ini kalo kamu inget) HEHE MAAF🙂 
                waktu itu kamu juga sempet cari kaos grey terus akhirnya nemu di cosmic (if im not mistaken yah). Naaah, now i gave you the other shade of grey color biar makin menggunung kaos-kaos collectionmu itu HEHEHH.
                Im sorryy kalo warnanya bukan color shade yang green-ish gitu yaa☹️ Semoga kamu sukaaa!!! </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif st.session_state.selected_gift == "PERFUME":
        st.markdown(
            """
            <div style="border-radius: 10px; padding: 20px; background: linear-gradient(to bottom, #d6d4d4, white); color: black; text-align: justify;">
                <div style="border-radius: 5px; padding: 20px; background: linear-gradient(to bottom, #d6d4d4, white); color: black; text-align: justify;">
                <p>    </p>
                <p>Here it is…. maleali yg kemaren kamu suka baunya itu. i gave you this biar kamu ngga nyesel-nyesel banget kalo beli parfum tapi ngga dipake sehari-hari banget (kalo misal bapak ngga cocok sama baunya)😁 
                Tapii, wear this perfume for yourself yaa ay, kalo kamu suka baunya yaa pake ajaa. You dont need to let other people decide what you should wear. Setiap orang kan juga punya seleranya masing-masingg, 
                jadi nggapapa kalo ada yang ngga suka sama apa yang kamu suka. SOO, if you like it then go for it ajah okay😉</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif st.session_state.selected_gift == "HEALTH KIT":
        st.markdown(
            """
            <div style="border-radius: 10px; padding: 15px; background: linear-gradient(to bottom, #d6d4d4, white); color: black; text-align: justify;">
                <div style="border-radius: 5px; padding: 20px; background: linear-gradient(to bottom, #d6d4d4, white); color: black; text-align: justify;">
                <p>    </p>
                <p>Health kit ini sebenernya inspired by kotak medis sih. Sekarang kan lagi musimnya orang sakit yaa, jadi aku bikinin kamu your personal medical box kalo kamu butuh waktu lagi kurang sehatt 
                (aku ngga doain sakit loh ya, sehat terus please jangan sakit😠). Trus kamu penasaran gak sih kenapa isinya ini? Kalo ngga ya gapapa sih tetep aku jelaskan sebagai berikut (kek laporan skripsi) :</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Dropdown untuk memilih item di health kit
        option = st.selectbox(
            "         "
            "Select one item yang mau kamu tau descriptionnya : ",
            ["Select item", "Inhaler Freshcare", "Salonpas", "Hansaplast", "Vitamin C"]
        )

        # Menampilkan deskripsi berdasarkan item yang dipilih
        descriptions = {
            "Inhaler Freshcare": "Since we have the same problem dengan dingin dan debu, I present to you the mighty✨INHALER FRESHCARE SMASH✨. Benda mini berwarna merah ini magic banget serius. "
                                "Kalo nanti kamu kena debu abis beberes rumah or kena dingin kehujanan gitu kamu langsung pake ini yah, "
                                "keburu makin mampet or meler hidungmuu. Semoga mini-mini cabe rawit ini bisa membantu ngurangin problem per-hidungmampet-an kamu (((aamiinn)))",

            "Salonpas": "Tiap kamu lagi ngga enak badan or meriang kan badanmu selalu ikut pegel-pegel juga ya, makanya aku siapin stock beberapa lembar koyo "
                        "biar nanti kamu tinggal ambil aja. Jadi one day kalo kamu tiba-tiba pegel ngga usah bingung beli koyo duluuu. "
                        "Jangan lupa tips n trick from me tentang teknik pemasangan koyo di saat pusing kepala ya😇",

            "Hansaplast": "Sebenernya hansaplast ini ngga butuh-butuh banget sih ya..... TAPI NGGA ADA YANG TAU LOH "
                        "kalo accidentally kegores something terus tiba-tiba berdarah gitu kan ya, kamu tinggal ambil dari health kit 😎😎 #kelazz",

            "Vitamin C": "Menurut riset yang telah kulakukan beberapa saat yang lalu, vitamin C ini tuh bisa mencegah sariawan loh??? "
                        "AS A PERSON WHO'S BEEN THROUGH A LOT (SERING SARIAWAN MAKSUDNYA) KAYAKNYA KAMU BUTUH BANGET DEH..... "
                        "Maaf yah adanya yang rasa lemon ini, yang jeruk ngga ada mulu soalnya hiks"
        }

        # Dictionary untuk gambar
        images = {
        "Inhaler Freshcare": "freshcare.jpg",
        "Salonpas": "salonpas.jpg",
        "Hansaplast": "hansaplast.jpg",
        "Vitamin C": "vitc.jpg"
    }
        
        if option != "Select item":
            col1, col2, col3 = st.columns([1.1, 3, 1])
            with col2:
                st.image(images[option], width=700)
            st.markdown(
                f"""
                <div style="border: 1px solid #ccc;  
                    padding: 35px; 
                    border-radius: 10px; 
                    background: white;  
                    color: black; 
                    text-align: justify; 
                    max-width: 1000px; 
                    margin: auto;">
                    <h4 style="text-align: center;">{option}</h4>
                    <p>{descriptions[option]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

page_names_to_funcs = {
    "Homepage": intro,
    "Wishes": wishes,
    "Gifts": gifts,
}

demo_name = st.sidebar.selectbox("WELCOME! Choose a page below!", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
