# Персонажи
define user = Character('[name]', color="#ffffff")
define d = Character('Организатор', color="#7fc7ff", image='director')
define e1 = Character('Лавочник', color="#00ff00", image='e1')
define e2 = Character('Девочка у стенда', color="#ffc0cb", image='e2')
define m = Character('[darkhair]', color="#8b00ff", image='dark')
# Музыка и звуки
define bg_music1 = 'game/audio/bg_music1.mp3'
define bg_music2 = 'game/audio/bg_music2.mp3'
define bg_music3 = 'game/audio/bg_music3.mp3'
define mini1 = 'game/audio/mini1.mp3'
define mini2 = 'game/audio/mini2.mp3'
# Спрайты
image director = 'game/images/director/director smile3.png'
image e1 = 'game/images/e1/e1 smile.png'
image dark = 'game/images/dark/dark sad2.png'
# Картинки

# Положения

init:

    $ lefter = Position(xalign=0.3, yalign=1.0)
    $ righter = Position(xalign=0.8, yalign=1.0)
    $ topleft = Position(xalign=0.2, yalign=0.0)
    $ point = 0
    $ wrong = 0
    $ false = True
    $ darkhair = 'Тёмноволосая'
    # Значения пазла
    $ m1 = Position(xalign=0.62, yalign=0.05)
    $ m2 = Position(xalign=0.8, yalign=0.05)
    $ m3 = Position(xalign=0.98, yalign=0.05)
    $ m4 = Position(xalign=0.62, yalign=0.27)
    $ m5 = Position(xalign=0.8, yalign=0.27)
    $ m6 = Position(xalign=0.98, yalign=0.27)
    $ m7 = Position(xalign=0.62, yalign=0.49)
    $ m8 = Position(xalign=0.8, yalign=0.49)
    $ m9 = Position(xalign=0.98, yalign=0.49)






# Начало
label start:

    # Встреча

    # Определение имени пользователя
    $ name = renpy.input("Как вас зовут?")

    d "Приветствую тебя, [name]."

    "{i}Почему я ничего не вижу?{/i}"

    d "Потому что на тебе повязка!"

    user "Ты мысли читать умеешь?"

    d "О чём это ты? Ладно, давай я её сниму."

    scene bg kreml
    show director smile3
    with Dissolve(2)
    queue music bg_music1

    user "Ого."

    d "Те... Тебе нравится?"

    user "Выглядит не плохо."

    d smile4 "Правда?! Я очень рада что тебе понравилось."

    user "А в честь чего такой праздник?"

    show director neutral1
    pause(2)

    d "Ты что, ещё не в курсе?"

    d "Этот фестиваль посвящён истории нашей страны."

    user "{cps=*0.25}Хммм…{/cps}"

    d "Что такое?"

    user "Как то я не заинтересован в данной теме."

    d sad1 "Ну ты чего?{w} Это же интереснейшая тема для изучения - наша великая родина."

    d smile2 "Идём, я проведу тебе экскурсию по главным датам нашей страны!"

    user "Ну, раз уж ты меня сюда привела, пошли."

    hide director
    with Dissolve(1)

    # Конец первой сцены






# История 862
label one:

    # 862 год

    scene bg way1
    show director smile1 at righter
    with Dissolve(2)

    d neutral2 "Ты знаешь с чего началась история России?"

    user "В школе когда то проходили, да я забыл уже."

    d "Тогда слушай. Начало наша история берет в  862 году."

    show rurik at topleft
    with Dissolve(2)

    d """

    Князь Рюрик — варяг, согласно древнерусским летописям, призванный вместе со своим
     родом представителями славянских племён для княжения в Новгороде в 862 году.

    Основал династию Рюриковичей, распространившую свою власть на восточнославянские
     племена и объединившую их в древнерусское государство со столицей в Новгороде.

    """

    user "Видно крутой был мужик."

    hide rurik
    with Dissolve(0.5)
    show vadimthebrave at topleft
    with moveinleft

    d "Рюрик смог удержаться у власти в Новгороде подавив восстание Вадима Храброго."

    hide vadimthebrave
    with moveoutleft

    d "Распространил влияние на города Муром, Ростов, Белозерск, Полоцк, Изборск."

    show rurikson at topleft
    with Dissolve(0.5)

    d "Правил 17 лет, оставив после себя сына Игоря и в качестве регента при нём — Олега Вещего."

    hide rurikson
    with Dissolve(0.5)

    d smile2  "О, а вон там стенд, посвящённый этой теме."

    hide director
    with moveoutright

    stop music fadeout 2.0

    user "Зачем же так бежать?"

    # Конец второй сцены






# Игра 862
label two:

    # Стенд с вопросами

    scene bg l1
    show director smile4 at lefter
    with Dissolve(1)

    user "Эй, не надо так быстро бегать, я уже не молодой."

    d "Ты младше меня, так что не прикидывайся стариком."

    user "Так что ты хотела мне тут показать?"

    queue music bg_music2

    show e1 smile at righter
    with Dissolve(1)

    d smile2 "На каждом стенде есть \"мини игры\", это основная особенноесть моего фестиваля."

    user "Это и есть главная особенность квест фестиваля..?"

    show director smile1

    e1 "Привествую вас, у меня, вам придется ответить на несложные вопросы. {i}Вы же запомнили все что вам говорилось?!{/t}"

    user "Думаю я все запомнил..."

    d smile2 "Давай поспорим, если ты наберешь больше чем я, то я угощаю тебя любым блюдом, идет?"

    user "Любым? Что ж, я в деле!"

    stop music fadeout 2.0
    queue music mini1

    # 1
    menu:

        "Какой год считается годом основания Руси?"

        "988":
            "{nw}"
        "862":
            $ point += 1
            $ false = False
        "1147":
            "{nw}"
        "952":
            "{nw}"

    if false:
        $ answer = "Ты ошибся, правильный ответ - 862 год."
        $ wrong += 1
        if wrong == 0:
            "{nw}"
        elif wrong < 2:
            e1 surprised "[answer]"
            d smile3 "{nw}"
        elif wrong <= 4 and wrong >= 2:
            e1 oops "[answer]"
            d sad2 "{nw}"
        else:
            stop music fadeout 5.0
            show e1 normalclose:
                xalign  0.8, yalign 0.0
            e1 normalclose "[answer]"
            d sad1 "{nw}"
    else:
        $ false = True


    # 2
    menu:

        "Кто был первым правителем?"

        "Князь Владимир":
            "{nw}"
        "Князь Всеволод":
            "{nw}"
        "Князь Рюрик":
            $ point += 1
            $ false = False
        "Княгиня Ольга":
            "{nw}"

    if false:
        $ answer = "Ты ошибся, правильный ответ - Князь Рюрик."
        $ wrong += 1
        if wrong == 0:
            "{nw}"
        elif wrong < 2:
            e1 surprised "[answer]"
            d smile3 "{nw}"
        elif wrong <= 4 and wrong >= 2:
            e1 oops "[answer]"
            d sad2 "{nw}"
        else:
            stop music fadeout 5.0
            show e1 normalclose:
                xalign  0.8, yalign 0.0
            e1 normalclose "[answer]"
            d sad1 "{nw}"
    else:
        $ false = True


    # 3
    menu:

        "Кем был Князь Рюрик до становления правителем?"

        "Варяг":
            $ point += 1
            $ false = False
        "Воевода":
            "{nw}"
        "Дворянин":
            "{nw}"
        "Боярин":
            "{nw}"

    if false:
        $ answer = "Ты ошибся, правильный ответ - Варяг."
        $ wrong += 1
        if wrong == 0:
            "{nw}"
        elif wrong < 2:
            e1 surprised "[answer]"
            d smile3 "{nw}"
        elif wrong <= 4 and wrong >= 2:
            e1 oops "[answer]"
            d sad2 "{nw}"
        else:
            stop music fadeout 5.0
            show e1 normalclose:
                xalign  0.8, yalign 0.0
            e1 normalclose "[answer]"
            d sad1 "{nw}"
    else:
        $ false = True


    # 4
    menu:

        "Первая столица Древней Руси?"

        "Москва":
            "{nw}"
        "Киев":
            "{nw}"
        "Санкт-Петербург":
            "{nw}"
        "Новгород":
            $ point += 1
            $ false = False

    if false:
        $ answer = "Ты ошибся, правильный ответ - Новгород."
        $ wrong += 1
        if wrong == 0:
            "{nw}"
        elif wrong < 2:
            e1 surprised "[answer]"
            d smile3 "{nw}"
        elif wrong <= 4 and wrong >= 2:
            e1 oops "[answer]"
            d sad2 "{nw}"
        else:
            stop music fadeout 5.0
            show e1 normalclose:
                xalign  0.8, yalign 0.0
            e1 normalclose "[answer]"
            d sad1 "{nw}"
    else:
        $ false = True


    # 5
    menu:

        "Кто поднял восстание против Рюрика?"

        "Игорь Рюрикович":
            "{nw}"
        "Вадим Храбрый":
            $ point += 1
            $ false = False
        "Степан Разин":
            "{nw}"
        "Олег Вещий":
            "{nw}"

    if false:
        $ answer = "Ты ошибся, правильный ответ - Вадим Храбрый."
        $ wrong += 1
        if wrong == 0:
            "{nw}"
        elif wrong < 2:
            e1 surprised "[answer]"
            d smile3 "{nw}"
        elif wrong <= 4 and wrong >= 2:
            e1 oops "[answer]"
            d sad2 "{nw}"
        else:
            stop music fadeout 5.0
            show e1 normalclose:
                xalign  0.8, yalign 0.0
            e1 normalclose "[answer]"
            d sad1 "{nw}"
    else:
        $ false = True


    # 6
    menu:

        "Сколько лет правил князь Рюрик?"

        "17":
            $ point += 1
            $ false = False
        "9":
            "{nw}"
        "19":
            "{nw}"
        "15":
            "{nw}"

    if false:
        $ answer = "Ты ошибся, правильный ответ - 17 лет."
        $ wrong += 1
        if wrong == 0:
            "{nw}"
        elif wrong < 2:
            e1 surprised "[answer]"
            d smile3 "{nw}"
        elif wrong <= 4 and wrong >= 2:
            e1 oops "[answer]"
            d sad2 "{nw}"
        else:
            stop music fadeout 5.0
            show e1 normalclose:
                xalign  0.8, yalign 0.0
            e1 normalclose "[answer]"
            d sad1 "{nw}"
    else:
        $ false = True


    # 7
    menu:

        "Как звали сына Рюрика?"

        "Олег":
            "{nw}"
        "Вадим":
            "{nw}"
        "Владимир":
            "{nw}"
        "Игорь":
            $ point += 1
            $ false = False

    if false:
        $ answer = "Ты ошибся, правильный ответ - Игорь."
        $ wrong += 1
        if wrong == 0:
            "{nw}"
        elif wrong < 2:
            e1 surprised "[answer]"
            d smile3 "{nw}"
        elif wrong <= 4 and wrong >= 2:
            e1 oops "[answer]"
            d sad2 "{nw}"
        else:
            stop music fadeout 5.0
            show e1 normalclose:
                xalign  0.8, yalign 0.0
            e1 normalclose "[answer]"
            d sad1 "{nw}"
    else:
        $ false = True


    # Подсчёт
    if point < 3:
        d "Я немного расстроена насчет твоего результата…"
        e1 normal "[user] я расстроен насчет тебя, я думал ты умеешь слушать что тебе говорят."
        $ success = 'false'

    elif point > 5:
        d smile4 "Ого… ты молодец! Я такого даже не ожидала."
        e1 smile2 "Молодец! Я знал что друг директора не ошибется."
        $ success = 'true'

    else:
        d "Молодец, думаю каждый может ошибаться."
        e1 "Я бы посоветовал тебе выпить таблеток для памяти. Но даже так ты справился не плохо."
        $ success = 'mb'

    d smile2 "Ну что, пошли дальше?"

    # Конец третьей сцены






# История Москвы
label three:

    # Путь к Москве
    scene bg way1
    show director smile1
    with Dissolve(1)


    user """
    Дверь открыли 1.5 раза.\n{w}
    - \"Вот это да\" - сказал Штирлиц.\n{w}
    - \"TypeError: Fade(1.5) takes at least 3 arguments (3 given)\" - ответил компилятор.
    """

    d neutral2 "Что это?"

    user "Да так."

    queue music bg_music1

    d smile2 "Ну как тебе?"

    user "Было интересно, но я уже хочу уйти."

    d smile1 "Останься еще ненадолго, впереди будет еще больше и веселее.{w} Следующая станция -  1147 Первое упоминание о Москве!{w} {cps=*0.1}Чу-чу{/cps}."

    user "Можешь так больше не делать…"

    d smile4 "Я подумала так будет веселее…"

    # Конец третьей сцены






# Игра Москва
label four:

    scene bg l2
    show director smile1 at lefter
    show e2 at righter
    with Dissolve(1)

    d  "А вот и он!"

    user  "Что мне тут расскажут?"

    d  "{cps=*.5}А знаешь ли ты как устроена Москва{/cps}{nw}"

    user "Да"

    d sad2 "{cps=*.5}А… {w} ну…{w} А как она была построена ты знаешь?{/cps}{nw}"

    user "Не интересовался"

    d smile2  "Давай изучим этот вопрос! Наш прошлый спор в силе?"

    user "На этот раз так легко ты меня не проведешь."

    d smile4 "Я куплю два, если победишь меня здесь."

    user "Я учавствую!"

    e2 "Здравстуйте, вы хотели бы услышать историю нашей столицы?"

    show director smile1

    user "Почему бы и нет."

    e2 "Далекий-далекий 1147 год.{w} На крутом холме над рекой начинает свою историю древний город Москва."

    user "Похоже это надолго...{nw}"

    d "Слушай."

    stop music fadeout 25.0

    e2 """

    При раскопках в Московском Кремле были обнаружены артефакты, свидетельствующие о существовании Москвы в конце XI века.

    Это были свинцовая печать, датируемая между 1093 и 1096 годами, печатью скрепляли грамоты.

    Но еще большим фактом было выявление наличие рва, защищавшего поселение в XI-XII веках.

    """

    "{i}Похоже мы здесь застряли...{/t}"

    e2 "{cps=*1.2}В XIV веке Москва стала стремительно меняться.{w} Стены крепости московской при Иване Калите перестроили на новые —  дубовые, а к 1367 году по указу князя Дмитрия Донского были возведены белокаменные стены.{/cps}"

    e2 "{cps=*1.5}Вместе с Кремлем росли поселения и на земле вокруг стен, поднялся посад, в конце XIV века обнесенный валом со рвом.{/cps}"

    "{i}Уже сложно воспринимать информацию{/i}"

    e2 """

    {cps=*2}На посаде выросли Рождественский, Высокопетровский и Сретенский монастыри, которые проложили улицы между посадами и тропинки к селам и разбитым по округе поселениям.{/cps}

    {cps=*2.5}Выстраивались монастыри и за пределами посадов —  Андроньевский со Спасским собором, Симонов монастырь.{/cps}

    """

    user "Думаю нам хватит этой информации, спасибо."

    e2 "{cps=*2}Но это только начало...{/cps}{nw}"

    d smile4 "Ой, простите но нам надо спешить, давайте приступим к игре."

    play music mini2

    hide director
    with moveoutleft

    show moskov:
        xalign 0.1, yalign 0.4
    with Dissolve(1)

    e2 "Внимательно рассмотри и запомни эту картинку."

    e2 "Суть моего квеста - сбор пазла.{w} Надёюсь ты не ошибёшься и соберёшь его правильно!"

    e2 "Во время сбора тебе надо будет называть мне последовательность букв для каждой позиции."

    e2 "Позиции нумеруются слева направо так:\n   1, 2, 3 - верхний ряд\n   4, 5, 6 - средний ряд\n   7, 8, 9 - нижний ряд."

    "{i}Звучит просто.{/i}"

    menu:

        e2 "Готов?"

        "Да":
            scene bg l2
            with Dissolve(1)

    show g:
        xalign 0.02, yalign 0.6 # 7
    show e:
        xalign 0.22, yalign 0.35 # 5
    show c:
        xalign 0.42, yalign 0.1 # 3
    show i:
        xalign 0.42, yalign 0.6 # 9
    show d:
        xalign 0.02, yalign 0.35 # 4
    show b:
        xalign 0.22, yalign 0.1 # 2
    show a:
        xalign 0.02, yalign 0.1 # 1
    show f:
        xalign 0.42, yalign 0.35 # 6
    show h:
        xalign 0.22, yalign 0.6 # 8


    # 1
    $ lit = renpy.input("Назови букву для первой позиции")

    if lit == 'a':
        hide a
        show a at m1
        with Dissolve(0.5)

    elif lit == 'b':
        hide b
        show b at m1
        with Dissolve(0.5)

    elif lit == 'c':
        hide c
        show c at m1
        with Dissolve(0.5)

    elif lit == 'd':
        hide d
        show d at m1
        with Dissolve(0.5)

    elif lit == 'e':
        hide e
        show e at m1
        with Dissolve(0.5)

    elif lit == 'f':
        hide f
        show f at m1
        with Dissolve(0.5)

    elif lit == 'g':
        hide g
        show g at m1
        with Dissolve(0.5)

    elif lit == 'h':
        hide h
        show h at m1
        with Dissolve(0.5)

    elif lit == 'i':
        hide i
        show i at m1
        with Dissolve(0.5)


    # 2
    $ lit = renpy.input("Назови букву для второй позиции")

    if lit == 'a':
        hide a
        show a at m2
        with Dissolve(0.5)

    elif lit == 'b':
        hide b
        show b at m2
        with Dissolve(0.5)

    elif lit == 'c':
        hide c
        show c at m2
        with Dissolve(0.5)

    elif lit == 'd':
        hide d
        show d at m2
        with Dissolve(0.5)

    elif lit == 'e':
        hide e
        show e at m2
        with Dissolve(0.5)

    elif lit == 'f':
        hide f
        show f at m2
        with Dissolve(0.5)

    elif lit == 'g':
        hide g
        show g at m2
        with Dissolve(0.5)

    elif lit == 'h':
        hide h
        show h at m2
        with Dissolve(0.5)

    elif lit == 'i':
        hide i
        show i at m2
        with Dissolve(0.5)


    # 3
    $ lit = renpy.input("Назови букву для третьей позиции")

    if lit == 'a':
        hide a
        show a at m3
        with Dissolve(0.5)

    elif lit == 'b':
        hide b
        show b at m3
        with Dissolve(0.5)

    elif lit == 'c':
        hide c
        show c at m3
        with Dissolve(0.5)

    elif lit == 'd':
        hide d
        show d at m3
        with Dissolve(0.5)

    elif lit == 'e':
        hide e
        show e at m3
        with Dissolve(0.5)

    elif lit == 'f':
        hide f
        show f at m3
        with Dissolve(0.5)

    elif lit == 'g':
        hide g
        show g at m3
        with Dissolve(0.5)

    elif lit == 'h':
        hide h
        show h at m3
        with Dissolve(0.5)

    elif lit == 'i':
        hide i
        show i at m3
        with Dissolve(0.5)


    # 4
    $ lit = renpy.input("Назови букву для четвёртой позиции")

    if lit == 'a':
        hide a
        show a at m4
        with Dissolve(0.5)

    elif lit == 'b':
        hide b
        show b at m4
        with Dissolve(0.5)

    elif lit == 'c':
        hide c
        show c at m4
        with Dissolve(0.5)

    elif lit == 'd':
        hide d
        show d at m4
        with Dissolve(0.5)

    elif lit == 'e':
        hide e
        show e at m4
        with Dissolve(0.5)

    elif lit == 'f':
        hide f
        show f at m4
        with Dissolve(0.5)

    elif lit == 'g':
        hide g
        show g at m4
        with Dissolve(0.5)

    elif lit == 'h':
        hide h
        show h at m4
        with Dissolve(0.5)

    elif lit == 'i':
        hide i
        show i at m4
        with Dissolve(0.5)


    # 5
    $ lit = renpy.input("Назови букву для пятой позиции")

    if lit == 'a':
        hide a
        show a at m5
        with Dissolve(0.5)

    elif lit == 'b':
        hide b
        show b at m5
        with Dissolve(0.5)

    elif lit == 'c':
        hide c
        show c at m5
        with Dissolve(0.5)

    elif lit == 'd':
        hide d
        show d at m5
        with Dissolve(0.5)

    elif lit == 'e':
        hide e
        show e at m5
        with Dissolve(0.5)

    elif lit == 'f':
        hide f
        show f at m5
        with Dissolve(0.5)

    elif lit == 'g':
        hide g
        show g at m5
        with Dissolve(0.5)

    elif lit == 'h':
        hide h
        show h at m5
        with Dissolve(0.5)

    elif lit == 'i':
        hide i
        show i at m5
        with Dissolve(0.5)


    # 6
    $ lit = renpy.input("Назови букву для шестой позиции")

    if lit == 'a':
        hide a
        show a at m6
        with Dissolve(0.5)

    elif lit == 'b':
        hide b
        show b at m6
        with Dissolve(0.5)

    elif lit == 'c':
        hide c
        show c at m6
        with Dissolve(0.5)

    elif lit == 'd':
        hide d
        show d at m6
        with Dissolve(0.5)

    elif lit == 'e':
        hide e
        show e at m6
        with Dissolve(0.5)

    elif lit == 'f':
        hide f
        show f at m6
        with Dissolve(0.5)

    elif lit == 'g':
        hide g
        show g at m6
        with Dissolve(0.5)

    elif lit == 'h':
        hide h
        show h at m6
        with Dissolve(0.5)

    elif lit == 'i':
        hide i
        show i at m6
        with Dissolve(0.5)


    # 7
    $ lit = renpy.input("Назови букву для седьмой позиции")

    if lit == 'a':
        hide a
        show a at m7
        with Dissolve(0.5)

    elif lit == 'b':
        hide b
        show b at m7
        with Dissolve(0.5)

    elif lit == 'c':
        hide c
        show c at m7
        with Dissolve(0.5)

    elif lit == 'd':
        hide d
        show d at m7
        with Dissolve(0.5)

    elif lit == 'e':
        hide e
        show e at m7
        with Dissolve(0.5)

    elif lit == 'f':
        hide f
        show f at m7
        with Dissolve(0.5)

    elif lit == 'g':
        hide g
        show g at m7
        with Dissolve(0.5)

    elif lit == 'h':
        hide h
        show h at m7
        with Dissolve(0.5)

    elif lit == 'i':
        hide i
        show i at m7
        with Dissolve(0.5)


    # 8
    $ lit = renpy.input("Назови букву для восьмой позиции")

    if lit == 'a':
        hide a
        show a at m8
        with Dissolve(0.5)

    elif lit == 'b':
        hide b
        show b at m8
        with Dissolve(0.5)

    elif lit == 'c':
        hide c
        show c at m8
        with Dissolve(0.5)

    elif lit == 'd':
        hide d
        show d at m8
        with Dissolve(0.5)

    elif lit == 'e':
        hide e
        show e at m8
        with Dissolve(0.5)

    elif lit == 'f':
        hide f
        show f at m8
        with Dissolve(0.5)

    elif lit == 'g':
        hide g
        show g at m8
        with Dissolve(0.5)

    elif lit == 'h':
        hide h
        show h at m8
        with Dissolve(0.5)

    elif lit == 'i':
        hide i
        show i at m8
        with Dissolve(0.5)


    # 9
    $ lit = renpy.input("Назови букву для девятой позиции")

    if lit == 'a':
        hide a
        show a at m9
        with Dissolve(0.5)

    elif lit == 'b':
        hide b
        show b at m9
        with Dissolve(0.5)

    elif lit == 'c':
        hide c
        show c at m9
        with Dissolve(0.5)

    elif lit == 'd':
        hide d
        show d at m9
        with Dissolve(0.5)

    elif lit == 'e':
        hide e
        show e at m9
        with Dissolve(0.5)

    elif lit == 'f':
        hide f
        show f at m9
        with Dissolve(0.5)

    elif lit == 'g':
        hide g
        show g at m9
        with Dissolve(0.5)

    elif lit == 'h':
        hide h
        show h at m9
        with Dissolve(0.5)

    elif lit == 'i':
        hide i
        show i at m9
        with Dissolve(0.5)

    user "Так, вроде справился"

    hide a
    hide b
    hide c
    hide d
    hide e
    hide f
    hide g
    hide h
    hide i
    with moveoutright

    show e2
    with Dissolve(1)

    e2 "Так, посмотрим что у тебя получилось."

    stop music fadeout 5.0

    user "А где она?"

    e2 "А, кто?"

    show blackscreen
    with Dissolve(1)

    e2 "Ты куда побежал?"


    # Конец четвёртой сцены





# Встреча с тёмноволосой
label five:

    scene bg l3
    show director annoyed1
    with Dissolve(1)

    user "Что с лицом?"

    d neutral2 "У меня появились важные дела, не мог бы ты подождать меня здесь некоторое время?"

    user "Думаю я не потеряюсь."

    d smile1 "Отлично, увидимся."

    hide director
    with moveoutleft

    pause 1

    "{i}И сколько же мне её ждать придётся?{/i}"

    pause 1

    show blackscreen
    with Dissolve(0.25)

    hide blackscreen
    show dark sad2
    with Dissolve(0.25)

    pause .5

    queue music bg_music3

    "{i}Ого...{/i}"

    m sad1 "Эй парень, это сейчас был организатор?"
    user "Да, подруга моего детства."

    menu:

        m "Слушай, если ты с ней дружишь то и на мероприятии должен ориентироваться хорошо?"

        "Помочь":
            $ helped = True
            jump help

        "Не помогать":
            $ helped = False
            jump nohelp





# Если помочь
label help:

    user "Ну.. можно и так сказать."

    m smile2 "Отлично! Меня попросили подготовить презентацию к одной из дат истории, но я потерялась и не знаю где находится стенд \"Монголо-татарское Иго\"."

    user "Что ж... давай я проведу тебя к нему."

    "{i}Куда ты ее проведешь дурень?{/i}"

    show blackscreen
    with Dissolve(2)

    pause 1

    "{cps=*.1}Спустя 10 минут{/cps}"

    pause 0.5

    scene bg crowd
    show dark smile1
    with Dissolve(2)


    m "Спасибо тебе, ты мне очень помог."

    user "Да не за что. Честно говоря, я сам не знал где он находится..."

    m neutral2 "{cps=*0.5}О... Вот как...{/cps}{w} Ну ладно, зато вдвоем было веселее искать"

    user "Хмм...{w} этот стенд выглядит интересно, ты его подготовила?"

    m neutral1 "Да, это моя гордость, хочешь я тебе расскажу про свою дату?"

    user "Все равно мне делать нечего, так что валяй"

    m """

    Ведомые внуком великого Чингисхана, хана Бату, монголы стремились захватить или уничтожить всё на своём пути.

    Русские князья понимали, что рано или поздно придёт очередь их земель, и решили нанести удар первыми.

    """

    "{i}Я зря согласился... На одни и теже грабли...{/i}"

    m """
    В 1223 году русские войска вместе с половецкими кочевниками попытались остановить Батыя в Приазовье, на реке Калка, но проиграли.

    Причём со стороны монгольского войска это была лишь разведка. В последующие 14 лет монголы всё ближе подходили к русским границам, подчиняя соседние народы.

    Через 100 лет после Куликовской битвы, в 1480 году, ордынскому игу пришёл конец. Золотая Орда распалась на несколько ханств, и великий князь московский Иван III отказался выплачивать дань.

    Хан Большой Орды Ахмат снарядил поход на Русь, но русское войско остановило его на реке Угра. Этот эпизод вошёл в историю как «великое стояние на Угре».

    Несколько месяцев две армии стояли на противоположных берегах реки, не решаясь переходить в наступление. С приходом холодов Ахмат решил отступить.

    Больше ордынские войска на русских землях не появлялись.

    """

    user "Я думаю с меня достаточно.{w} Я наверное пойду."

    m neutral2 "Тогда до встречи, мне ещё надо тут кое-что подправить."

    user "Пока, пойду найду свою подругу."

    stop music fadeout 2.0

    show blackscreen
    with Dissolve(1)

    if success == 'true':
        jump end_ex
    elif success == 'mb':
        jump end_good
    else:
        jump end_bad




# Если не помогать
label nohelp:

    user "Вообще-то я тоже слабо здесь ориентируюсь."

    m "Правда? А я думала что ты должен знать...{w}  Ну ладно, пойду поищу сама…"

    user "Пока..."

    hide dark
    with Dissolve(1)
    stop music fadeout 5.0

    "{i}Может стоило попытаться помочь...{/i}"

    if success == 'true':
        jump end_good
    else:
        jump end_bad





# Концовки





# Оличная концовка
label end_ex:

    scene bg l3
    show director neutral1
    with Dissolve(1)

    user "А вот ты где, я тебя повсюду искал."

    d neutral2 "Я думала ты уже ушел. Где ты был."

    user "Я помогал тут одному человеку. Так что мы собираемся теперь делать?"

    d smile2 "Ну... решай сам."

    user "Ты мне обещала меня накормить, помнишь?"

    d smile4 "Получается с меня два блюда? Что ж пошли поедим, ты все таки устал."

    show dark smile1:
        xalign -0.25 yalign 1.0
    with moveinleft

    m "Ребята, привет!"

    d "Ох, Сатоми, привет, давно не виделись, как там твой стенд?"

    $ darkhair = 'Сатоми'

    show dark smile2:
        xalign 0.15 yalign 1.0
    with moveinleft

    m "Вобще-то я потерялась в начале, но твой друг помог мне."

    d "Правда? Какой же ты у меня добрый!"

    user "Спасибо..."

    d "Пошлите тогда вместе, Сатоми, ты же тоже проголодалась?"

    m "Пошли, я как раз собиралась посетить одно местечко, думаю вам понравиться"

    show blackscreen
    with Dissolve(3)

    return




# Хорошая концовка
label end_good:

    if helped:

        scene bg l3
        with Dissolve(2)

        user "Странно, она уже должна была быть тут..."

        m "Ээээй."

        queue music bg_music3

        pause .5

        show blackscreen
        with Dissolve(0.25)

        hide blackscreen
        show dark smile1
        with Dissolve(1)

        user "Что ты тут делаешь?"

        m smile2 "Я со всем закончила и пришла прогуляться с тобой.{w} А где твоя подруга?"

        user "Не знаю, мы договорились встретиться на этом же месте. Может она уже ушла?"

        m "Пошли тогда поищем ее вместе, я видела как она проходила к стенду 42-ого года."

        user "Пошли, может ей нужна помощь."

        show dark smile1

        show blackscreen
        with Dissolve(3)

        stop music fadeout 2.0

        return


    else:

        pause 1

        scene bg l3
        show director neutral1

        user "Вот ты где! Чего ты так долго?"

        d smile2 "Пришлось помогать одной знакомой, она потерялась и пришлось ее провожать."

        user "А... Понятно..."

        d smile4 "Чего ты такое хмурый стал? Проголодался может? Пошли накормлю тебя, я же все таки обещала."

        user "Пошли, может я и вправду проголодался..."

        show blackscreen
        with Dissolve(3)

    return





# Плохая концовка
label end_bad:

    show blackscreen
    with Dissolve(2)

    pause 1

    scene bg l3
    with Dissolve(2)

    user "Что-то ее долго нет. Хммм…. может пойти поискать ее."

    pause 1

    show blackscreen
    with Dissolve(2)

    pause .5

    scene bg crowd
    with Dissolve(2)

    pause 1

    user "Да где же она."

    pause .5

    scene blackscreen
    with Dissolve(2)

    pause 1

    scene bg way1
    with Dissolve(2)

    pause 1

    user "Дьявол, прошло уже больше получаса. Становится скучновато."

    pause .5

    scene blackscreen
    with Dissolve(1)

    pause 1

    scene bg kreml
    with Dissolve(2)

    pause 1

    user "Пойду домой тогда."

    pause .5

    scene blackscreen
    with Dissolve(3)
