import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json
TOKEN="8101101098:AAFuHYiZfuSgrc0-5JUWqjn9nvtBFkUo-Y4"
bot=telebot.TeleBot(TOKEN,parse_mode=None)
user_passwords = {}
def load_txt():
    with open("txt.json", "r", encoding="utf-8") as file:
        return json.load(file)
txt = load_txt()

@bot.message_handler(commands=['start'])
def send_txt(message):
    bot.send_message(message.chat.id, "大家好啊我是豆沙包，不知道為什麼明明是寒假我還要可撥的被人類壓榨嗚嗚嗚")
    bot.send_message(message.chat.id, "接下來的這趟旅途我會一直陪伴大家，也會不斷給各位發布任務和提示，接下來是RPG遊戲規則介紹，要仔細閱讀喔！")
    bot.send_message(message.chat.id, "1.這次的遊戲會直接給玩家分發地圖自由活動，每個場地都可以重複過去遊玩，至少要幫npc完成一個任務才能擁有線索，也可以積累積分點，根據任務完成度不同，可以獲得的線索數量也不同，當然，也可以重複挑戰任務，但不可以連續重複挑戰同一角色的任務")
    bot.send_message(message.chat.id, "2.線索一次只能選一個地方拿，例如教室和辦公室，雖然同樣在學校，但一次只能選一個地方")
    bot.send_message(message.chat.id, "3.拿到道具(線索)後可以選擇拍照傳群組，不可以拿走道具，每得到一個線索，都會有一個提示詞，只要輸入提示即可從機器人身上拿到完整劇情線索")
    bot.send_message(message.chat.id, "4.遊玩過程會不定時啟動臨時任務，完成任務可以獲得積分點")
    bot.send_message(message.chat.id, "5.積分點除了在最後結算有加成外，也可以拿來購買線索")
    bot.send_message(message.chat.id, "6.每小都有一次對外求助機會，積分點達到一定數額也可以兌換求助，求助內容是關於劇情推測相關的內容")
    bot.send_message(message.chat.id, "7.如果有需要的話，可以隨時給阿潛發訊息或打電話，在搜索過程中他會不停走動，想找到他也是有難度的喔！")
    bot.send_message(message.chat.id, "8.遊戲時間是有限制的，時間到便會強制結束，並發放劇情相關題目，真相及結局選擇會等所有小隊作答完畢後統一發放")
    bot.send_message(message.chat.id, "9.我們的最終結算包含積分、劇情選擇、問卷，問卷部分會詢問有關於劇情的問題，所以一定要還原故事真相喔！")
    bot.send_message(message.chat.id, "豆沙包就先在這裡祝大家玩得愉快啦！這次要進入的故事名叫「雙生花」，是可憐的豆沙包趕工出來的遊戲，不要嫌棄它不然我會很杯桑喔！")

@bot.message_handler(commands=['開始遊戲'])
def send_txt(message):
    text1 = txt.get("first", "沒有找到相關的文章。")
    text2 = txt.get("second", "沒有找到相關的文章。")
    text3 = txt.get("third", "沒有找到相關的文章。")
    text4 = txt.get("forth", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)
    bot.send_message(message.chat.id, text3)
    bot.send_message(message.chat.id, text4)

@bot.message_handler(commands=['初始資料'])
def send_txt(message):
    text1 = txt.get("村莊資料", "沒有找到相關的文章。")
    text2 = txt.get("調查資料", "沒有找到相關的文章。")
    text3 = txt.get("繼續看故事", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)
    bot.send_message(message.chat.id, text3)

@bot.message_handler(commands=['繼續看故事'])
def send_txt(message):
    text1 = txt.get("fifth", "沒有找到相關的文章。")
    text2 = txt.get("six", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)
    bot.send_message(message.chat.id, "請問那女孩與死者是什麼關係？",reply_markup=gen_markup())

def gen_markup():
    markup=InlineKeyboardMarkup()
    markup.row_width=2
    markup.add(InlineKeyboardButton("雙胞胎",callback_data="dif"),
               InlineKeyboardButton("她們是同一人",callback_data="same"),
               )
    return markup

def disable_markup():
    """生成已禁用的按鈕"""
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("知道你想改答案但你不能改哈", callback_data="disabled")
    )
    return markup

@bot.callback_query_handler(func=lambda call:call.data in ["dif", "same"])
def callback_query(call):
    player_choice=call.data
    if player_choice == "disabled":
        bot.answer_callback_query(call.id, "知道你想改答案但你不能改哈")
        return
    if player_choice == "dif":
        reply_message = "恭喜答對，請輸入/繼續"
    elif player_choice == "same":
        reply_message = "錯誤的答案！請輸入/繼續"
    bot.send_message(call.message.chat.id, reply_message)
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=disable_markup()
        )
    
@bot.message_handler(commands=['繼續'])
def send_txt(message):
    text1 = txt.get("seven", "沒有找到相關的文章。")
    text2 = txt.get("eight", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)
    bot.send_message(message.chat.id, "請選擇搜索地點(輸入時在地點前記得加上/)")
    bot.send_message(message.chat.id, "落井小學\n沉魚診所\n許願井\n住宅區")

@bot.message_handler(commands=['落井小學'])
def send_txt(message):
    text1 = txt.get("school", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, "選擇要去學校的哪裡？")
    bot.send_message(message.chat.id, "教室\n教師辦公室")

@bot.message_handler(commands=['教室'])
def send_txt(message):
    text1 = txt.get("classroom", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['查看黑板'])
def send_txt(message):
    text1 = txt.get("blackboard", "沒有找到相關的文章。")
    text2 = txt.get("blackboard_memory", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['觀察桌子'])
def send_txt(message):
    text1 = txt.get("table", "沒有找到相關的文章。")
    text2 = txt.get("table_memory", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['打開林雪的置物櫃'])
def send_txt(message):
    text1 = txt.get("snow_locker", "沒有找到相關的文章。")
    text2 = txt.get("snow_locker_memory", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['打開林玄的置物櫃'])
def send_txt(message):
    text1 = txt.get("black_locker", "沒有找到相關的文章。")
    text2 = txt.get("black_locker_memory", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['瀏覽值日表'])
def send_txt(message):
    text1 = txt.get("duty", "沒有找到相關的文章。")
    text2 = txt.get("duty_memory", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['發現藝術角'])
def send_txt(message):
    text1 = txt.get("art", "沒有找到相關的文章。")
    text2 = txt.get("art_memory", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['教師辦公室'])
def send_txt(message):
    text2 = txt.get("office", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['觀察合照'])
def send_txt(message):
    text2 = txt.get("photo", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['偷瞄快遞箱'])
def send_txt(message):
    text2 = txt.get("delivery", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['發現小羊吊飾'])
def send_txt(message):
    text2 = txt.get("sheep", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['沉魚診所'])
def send_txt(message):
    text1 = txt.get("clinic", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, "選擇要去診所的哪裡？")
    bot.send_message(message.chat.id, "余醫生的診間\n余醫生的房間")

@bot.message_handler(commands=['余醫生的診間'])
def send_txt(message):
    text1 = txt.get("clinic_room", "沒有找到相關的文章。")
    text2 = txt.get("clinic_room_sec", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['林雪的病歷表'])
def send_txt(message):
    text1 = txt.get("snow_sick", "沒有找到相關的文章。")
    text2 = txt.get("snow_sick_scr", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['查看林玄的病歷表'])
def send_txt(message):
    text1 = txt.get("black_sick", "沒有找到相關的文章。")
    text2 = txt.get("black_sick_scr", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['瀏覽顏徽的病歷表'])
def send_txt(message):
    text1 = txt.get("clr_sick", "沒有找到相關的文章。")
    text2 = txt.get("clr_sick_scr", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['未知病歷表'])
def send_txt(message):
    text1 = txt.get("x_sick", "沒有找到相關的文章。")
    text2 = txt.get("x_sick_scr", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)

@bot.message_handler(commands=['余醫生的房間'])
def send_txt(message):
    text1 = txt.get("clinic_bedroom", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['被密碼鎖起的盒子'])
def send_txt(message):
    text1 = txt.get("0926_box", "沒有找到相關的文章。")
    text2 = txt.get("0926_box_name", "沒有找到相關的文章。")
    text3 = txt.get("0926_box_voice", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)
    bot.send_message(message.chat.id, text3)

@bot.message_handler(commands=['桌墊底下的報紙'])
def send_txt(message):
    text1 = txt.get("news", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['書架上有一本書不見了'])
def send_txt(message):
    text1 = txt.get("miss_book", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['紙條'])
def send_txt(message):
    text1 = txt.get("small_paper", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['離開診所'])
def send_txt(message):
    text1 = txt.get("leave_clinic", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['許願井'])
def send_txt(message):
    text1 = txt.get("wish", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['兩側的草叢'])
def send_txt(message):
    text1 = txt.get("grass", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['許願井內部'])
def send_txt(message):
    text1 = txt.get("inside", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['許願井外部'])
def send_txt(message):
    text1 = txt.get("outside", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['許願井井口'])
def send_txt(message):
    text1 = txt.get("top", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['住宅區'])
def send_txt(message):
    text1 = txt.get("house_area", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, "林家屋子\n村長家\n雜貨店\n酒吧")

@bot.message_handler(commands=['林家屋子'])
def send_txt(message):
    text1 = txt.get("lins_home", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, "客廳\n林玄房間\n林雪房間")

@bot.message_handler(commands=['客廳'])
def send_txt(message):
    text1 = txt.get("lins_home_livingroom", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['林玄房間'])
def send_txt(message):
    text1 = txt.get("lins_home_blackroom", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['林雪房間'])
def send_txt(message):
    text1 = txt.get("lins_home_snowroom", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['發現信封'])
def send_txt(message):
    text1 = txt.get("envelope", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['家庭訪問資料'])
def send_txt(message):
    text1 = txt.get("family_teacher", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['角落裡的棍子'])
def send_txt(message):
    text1 = txt.get("stick", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['林玄的衣櫃'])
def send_txt(message):
    text1 = txt.get("black_wardrobe", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['童話繪本'])
def send_txt(message):
    text1 = txt.get("storybook", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['盯著化妝鏡'])
def send_txt(message):
    text1 = txt.get("black_mirror", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['林雪的衣櫃'])
def send_txt(message):
    text1 = txt.get("snow_wardrobe", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['描寫藥物治療的書籍'])
def send_txt(message):
    text1 = txt.get("medi_book", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['日記本'])
def send_txt(message):
    text1 = txt.get("dairy", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['密碼盒'])
def send_txt(user_id):
    text1 = txt.get("password_box", "沒有找到相關的文章。")
    bot.send_message(user_id, text1)

@bot.message_handler(commands=['逃跑計畫'])
def send_txt(message):
    text1 = txt.get("escape_plan", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['三個音檔的錄音筆'])
def send_txt(message):
    text1 = txt.get("three_voice", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['藥品'])
def send_txt(message):
    text1 = txt.get("medicine", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['雜貨店'])
def send_txt(message):
    bot.send_message(message.chat.id, "這裡是沒有道具只有線索的雜貨店，但我們有更豐厚的積分等你喔親")

@bot.message_handler(commands=['酒吧'])
def send_txt(message):
    bot.send_message(message.chat.id, "這裡是沒有道具只有線索的酒吧，但我們有更豐厚的積分等你喔親")

@bot.message_handler(commands=['村長家'])
def send_txt(message):
    text1 = txt.get("leader_house", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, "輸入/進入村長房間")

@bot.message_handler(commands=['進入村長房間'])
def send_txt(message):
    text1 = txt.get("leader_bedroom", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['村長的衣櫃'])
def send_txt(message):
    text1 = txt.get("leader_wardrobe", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['手機的出現'])
def send_txt(message):
    text1 = txt.get("phone", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['盒裝煙火'])
def send_txt(message):
    text1 = txt.get("firework", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['手冊'])
def send_txt(message):
    text1 = txt.get("hand_book", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['禁令'])
def send_txt(message):
    text1 = txt.get("ban", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['打開衣櫃後的暗門'])
def send_txt(message):
    text1 = txt.get("dark_door", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)

@bot.message_handler(commands=['停止搜索'])
def send_txt(message):
    bot.send_message(message.chat.id, "時間到了！根據搜索到的線索還原真相囉！")

@bot.message_handler(commands=['結局公開'])

def send_txt(message):
    text1 = txt.get("end_first", "沒有找到相關的文章。")
    text2 = txt.get("end_second", "沒有找到相關的文章。")
    text3 = txt.get("end_third", "沒有找到相關的文章。")
    text4 = txt.get("end_forth", "沒有找到相關的文章。")
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)
    bot.send_message(message.chat.id, text3)
    bot.send_message(message.chat.id, text4)
    bot.send_message(message.chat.id, "(如果第一次就選到true end會另外加分喔！)")
    bot.send_message(message.chat.id, "點選按鈕以選擇結局",reply_markup=gen_markup2())

def gen_markup2():
    markup=InlineKeyboardMarkup()
    markup.row_width=1
    markup.add(InlineKeyboardButton("我還怨恨著她",callback_data="BE"),
               InlineKeyboardButton("大概能理解她了吧？",callback_data="NE"),
               InlineKeyboardButton("談不上什麼想法，她是我的姊姊，從始至終，都是如此",callback_data="TE"),
               )
    return markup

@bot.callback_query_handler(func=lambda call:call.data in ["BE", "NE", "TE"])
def callback_query_end(call):
    player_choice = call.data
    if player_choice == "BE":
        text1 = txt.get("be_first", "沒有找到相關的文章。")
        text2= txt.get("be_second", "沒有找到相關的文章。")
        bot.send_message(call.message.chat.id,text1)
        bot.send_message(call.message.chat.id,text2)
    elif player_choice == "NE":
        text1 = txt.get("ne_first", "沒有找到相關的文章。")
        text2= txt.get("ne_second", "沒有找到相關的文章。")
        bot.send_message(call.message.chat.id,text1)
        bot.send_message(call.message.chat.id,text2)
    elif player_choice == "TE":
        text1 = txt.get("te_first", "沒有找到相關的文章。")
        text2= txt.get("te_second", "沒有找到相關的文章。")
        text3 = txt.get("te_third", "沒有找到相關的文章。")
        text4= txt.get("te_forth", "沒有找到相關的文章。")
        text5 = txt.get("te_fifth", "沒有找到相關的文章。")
        text6= txt.get("te_six", "沒有找到相關的文章。")
        bot.send_message(call.message.chat.id,text1)
        bot.send_message(call.message.chat.id,text2)
        bot.send_message(call.message.chat.id,text3)
        bot.send_message(call.message.chat.id,text4)
        bot.send_message(call.message.chat.id,text5)
        bot.send_message(call.message.chat.id,text6)

@bot.message_handler(commands=['遊玩結束'])
def send_txt(message):
    bot.send_message(message.chat.id, "嘿嘿謝謝你們玩完了，豆沙包要下班啦哈哈哈......喔不對，我還有好幾天寒訓要參加嗚嗚嗚，我還是回家睡覺好了，掰掰")

@bot.message_handler(commands=['豆沙包'])
def send_txt(message):
    bot.send_message(message.chat.id, "蛤你叫我幹嘛，我一直給人當免費勞工已經夠可撥了你還打擾我")

@bot.message_handler(commands=['豆沙包你性別是什麼'])
def send_txt(message):
    bot.send_message(message.chat.id, "蛤我是豆沙包為什麼會有性別，你好怪喔！")

@bot.message_handler(commands=['豆沙包你覺得楓資誰最怪'])
def send_txt(message):
    bot.send_message(message.chat.id, "蛤不都是瘋子嗎全部都很怪")

@bot.message_handler(commands=['豆沙包你覺得吱吱腦子怎麼樣'])
def send_txt(message):
    bot.send_message(message.chat.id, "蛤應該不太行吧？")

@bot.message_handler(commands=['豆沙包你好可愛喔'])
def send_txt(message):
    bot.send_message(message.chat.id, "哼哼，那當然，我可是被長期壓榨後還能活在餐廳的存在")

@bot.message_handler(commands=['豆沙包你覺得千億姐姐怎麼樣'])
def send_txt(message):
    bot.send_message(message.chat.id, "咳咳，我不敢說我家老闆的壞話，但偷偷跟你們說喔！她好像跟我一樣被壓榨慘了")

@bot.message_handler(commands=['豆沙包你覺得蜜獾怎麼樣'])
def send_txt(message):
    bot.send_message(message.chat.id, "聽說嘎米很喜歡給人看奇怪的圖片，她怪怪的")

@bot.message_handler(commands=['豆沙包你怎麼一直爛掉'])
def send_txt(message):
    bot.send_message(message.chat.id, "我主人太弱了不能怪我嗚嗚嗚我也不想爛掉")

@bot.message_handler(commands=['豆沙包你怎麼一直當'])
def send_txt(message):
    bot.send_message(message.chat.id, "我好累，呼呼，我好想休息嗚嗚嗚")

@bot.message_handler(commands=['豆沙包你還在嗎'])
def send_txt(message):
    bot.send_message(message.chat.id, "可以不要再叫我了嗎嗚嗚，你們要壓榨我到什麼時候")

@bot.message_handler(commands=['豆沙包你要小心不要被吃掉'])
def send_txt(message):
    bot.send_message(message.chat.id, "不會啦我在餐桌上混跡多年，哪這麼容易被吃掉，而且我是疲憊的豆沙包不好吃嗚嗚")

@bot.message_handler(commands=['不會啦豆沙包你很好吃'])
def send_txt(message):
    bot.send_message(message.chat.id, "真的嗎嗚嗚嗚你真好，但不可以吃我喔！")

bot.infinity_polling()
