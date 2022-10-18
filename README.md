# File-Sharing-Forcesub2

Bot Telegram untuk menyimpan Posting atau File yang dapat Diakses melalui Link Khusus.
Saya Kira Ini Akan Bermanfaat Bagi Banyak Orang.

## ⚠️ Disclaimer

```
Saya tidak bertanggung jawab atas penyalahgunaan bot ini.
Bot ini dimaksudkan untuk membantu untuk menyimpan file yang diinginkan yang dapat diakses melalui Link Khusus.
Gunakan bot ini dengan risiko Anda sendiri, dan gunakan bot ini dengan bijak.
```

### Features
- Sepenuhnya dapat dicustom.
- Dapat di-deploy di heroku & vps.
- Pesan sambutan & Forcesub yang dapat dicustom.
- Lebih dari satu Posting dalam Satu Link (batch).
- Fleksibel FSUB Button bisa 1 button atau 2 button menyesuaikan dengan var yang di isi.

### Setup

- Tambahkan bot ke Channel Database dengan semua izin admin
- Tambahkan bot ke Channel ForceSub tambahkan bot sebagai ADMIN
- Tambahkan bot ke Group ForceSub tambahkan bot sebagai ADMIN

## 🛡 Installation
### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://risman.vercel.app/file-deploy.html)</br>

**Tonton Video Tutorial Ini di YouTube untuk Bantuan memasang di Heroku**<br>
<a href="https://youtu.be/O2tieQgzYZg">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>

<details>
<summary><h3><b>🔗 Extra Custom & List Vars</b></h3></summary>

### Variables

* `API_HASH` Dapatkan API HASH di web my.telegram.org.
* `API_ID` Dapatkan APP ID di web my.telegram.org
* `TG_BOT_TOKEN` Dapatkan dari t.me/BotFather
* `OWNER` Masukan Username Telegram untuk Owner BOT
* `CHANNEL_ID` Masukan ID Channel Untuk [Channel Database] contoh:- -100xxxxxxxx
* `ADMINS` Masukan User ID untuk mendapatkan hak Admin di BOT
* `START_MESSAGE` Opsional: Pesan /start memulai awalan ke bot, Gunakan <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#start_message'>format</a> parsemode HTML 
* `FORCE_SUB_MESSAGE` Opsional: Pesan Paksa Subscribe bot, Gunakan Format parsemode HTML
* `FORCE_SUB_CHANNEL` Masukan ID dari Channel Untuk Wajib Subscribenya
* `FORCE_SUB_GROUP` Masukan ID dari Group Untuk Wajib Subscribenya

### Extra Variables

* `CUSTOM_CAPTION` letakkan teks teks Kustom Anda jika Anda ingin Mengatur Teks Kustom, Anda dapat menggunakan HTML dan <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#custom_caption'>fillings</a> untuk pemformatan (hanya untuk dokumen)
* `DISABLE_CHANNEL_BUTTON` Masukan True untuk Nonaktifkan Tombol Berbagi Saluran, Default jika False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption
