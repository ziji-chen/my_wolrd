'''我的首页'''
import streamlit as st
from PIL import Image
import time

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区','更多应用','我知道点','我的地图'])


def page_1():
    '''我的兴趣推荐'''
    with open('霞光.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('slogan.png')
    tab1,tab2,tab3,tab4= st.tabs(['电影推荐','游戏推荐','书籍推荐','习题集推荐'])
    with tab1:
        st.write('策划的电影推荐：头号玩家')
        st.image('电影.png')
        st.write('-----------------------------')
    with tab2:
        st.write('策划的游戏推荐：暗区突围')
        st.image('游戏.png')
        st.write('-----------------------------')
    with tab3:
        st.write('策划的书籍推荐:三体')
        st.image('书籍.png')
        st.write('-----------------------------')
    with tab4:
        st.write('策划的习题集推荐：万唯中考')
        st.image('习题.png')
        st.write('-----------------------------')


def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        # tab1,tab2,tab3,tab4= st.tabs(['原色','改色1','改色2','改色3'])
        # with tab1:
        #     st.image(img)
        # with tab2:
        #     st.image(img_change(img,0,2,1))
        # with tab3:
        #     st.image(img_change(img,1,2,0))
        # with tab4:
        #     st.image(img_change(img,1,0,2))
        st.image(img)
        r = st.slider('R：', 1, 256,1)
        g = st.slider('G：', 1, 256,1)
        b = st.slider('B：', 1, 256,1)
        if r == 256 and g == 256 and b == 256:
            st.image('素材.png')
        else:
            st.image(img_change(img,r,g,b))
        


def page_3():
    '''我的智能词典'''
    st.write(':blue[智能词典]')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        roading = st.progress(0, '开始加载')#显示计时器
        for i in range(1, 101, 1):
            time.sleep(0.1)
            roading.progress(i, '正在加载'+str(i)+'%')
            roading.progress(100, '加载完毕，请等待结果展示')
        st.write(words_dict[word][1])
    #触发彩蛋
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
    if word == 'python':
        st.code('''
                #恭喜你触发彩蛋，这是一行python代码
                print('hello world')
                ''')
    if word == 'snow':
        st.snow()
    if word == 'birthday':
        st.balloons()
    if word == 'Peter':
        st.code('''
                访问者你好，不管你是有意还是无意进入这个网站，都是
                我们的缘分，如果网站有什么漏洞，欢迎向本策划指出。
                       1111       1111
                11111                   11111
                    1111             1111
                       1111       1111
                            11 11
                              1
                      （来自策划深深的爱）
                ''')

def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '策划':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '路人':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
        elif i[1] == '自定义':
            with st.chat_message('哈'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['策划','路人','自定义'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page_5():
    '''更多应用'''
    # 跳转按钮link_button()
    st.link_button('百度首页', 'https://www.baidu.com/')
    st.write('----')
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['编程猫社区', '我的bilibili','我的抖音'])
    if go == '编程猫社区':
        st.link_button('探索编程宇宙', 'https://shequ.codemao.cn/')
    elif go == '我的bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')
    elif go == '我的抖音':
        st.link_button('帮我点小红花', 'https://www.douyin.com/')
        
def page_6():
    '''我知道点'''
    st.write('----')
    st.write('你知道吗：为什么要设置公网和私网？为什么不让每一个设备都直接连接到公网上？')
    cb1 = st.checkbox('易于管理')
    cb2 = st.checkbox('效率高')
    cb3 = st.checkbox('网速快')
    cb4 = st.checkbox('安全性好')
    l = [cb1, cb2, cb3, cb4]
    if st.button('确认答案'):
        if True in l:
            st.write('其实都不对，答案是“历史问题，不得已而为之”，大家可以自己去了解哦')
        else:
            st.write('好厉害！确实都不对，真实答案是“历史问题，不得已而为之”，大家可以自己去了解哦')
    st.write('----')
    st.write('下面哪些小程序可以被嵌入网页中？')
    cb1 = st.checkbox('A.turtle绘图作品')
    cb2 = st.checkbox('B.图片处理工具')
    cb3 = st.checkbox('C.智能词典工具')
    cb4 = st.checkbox('D.pygame小游戏')
    b1 = st.button('第1题答案')
    if b1:
        if cb1 == False and cb2 == True and cb3 == True and cb4 == False:
            st.write('回答正确！')
        else:
            st.write('再想想')


def page_7():
    '''我的地图'''
    data = {'latitude': [37.7749, 34.0522, 40.7128], 
            'longitude': [(-122.4194), (-118.2437), (-74.006)],
            'name': ['San Francisco', 'Los Angeles', 'New York']}
    st.map(data, zoom=4, use_container_width=True)

            
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            # r = img_array[x, y][rc]
            # g = img_array[x, y][gc]
            # b = img_array[x, y][bc]
            img_array[x, y] = (rc, gc, bc)
    return img


if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '更多应用':
    page_5()
elif page == '我知道点':
    page_6()
elif page == '我的地图':
    page_7()