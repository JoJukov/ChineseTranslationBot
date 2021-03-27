from googletrans import Translator

tr = Translator()

think_positive = "Думай позитивно, стакан всегда наполовину полон, всегда\n" \
                 "Чувствуй хорошее, плохого не существует, между «нет» и «да» выбор только «да»\n" \
                 "Верь в лучшее, жизнь — это танец под присмотром чуткого Бога\n" \
                 "Повторяй эту поебень чаще; повторяй, даже если звучит убого"

goons = "Кость в кость, так повелось\n" \
        "Ну и последний васюня руку к арматуре\n" \
        "А я: «Ну, ты пиздец в натуре дурень, тыквой четче думай»\n" \
        "Вынул ножик, истыкал пиздюгана, дунул дури\n" \
        "Упали кони, подпустили вони, кто хрипит кто стонет\n" \
        "Не их был день\n" \
        "Раз в жизни случается такая хуетень"

losing_my_mind = "Теряю голову и постоянно хочу видеть\n" \
                 "Тебя голую или хотя бы топлесс\n" \
                 "Или хотя бы то, что видит пылесос\n" \
                 "Когда ты пылесосишь под диваном\n" \
                 "Или стать опытным шаманом\n" \
                 "Чтобы видеть тебя где бы ты ни была\n" \
                 "Приближаться, нюхать запах твоих волос\n" \
                 "От запаха этого сердце под землю, потом в небеса"

RON = "Разговоры о напасах сперва\n" \
      "Дым густой как сперма, нервы\n" \
      "Кто-то бежит, его закроют завтра\n" \
      "По бейсболке и отпечаткам\n" \
      "Кто-то лежит, внутри фенамин, на пальце печатка\n" \
      "Кого-то зарыли, кто-то воткнул под первым\n" \
      "Кровь толчками, лохи со стволами\n" \
      "Не умереть надо уметь, кровь на асфальте\n" \
      "Слишком часто жизнь помещается в гроб\n"

idk_why = "Я не знаю, почему ты читаешь рэп\n" \
          "Говоришь, что ты MC, но у тебя таланта нет\n" \
          "Не знаю, почему я водкой запиваю воду\n" \
          "Зачем ты педик суёшь себе самотык в жопу\n" \
          "Не знаю, почему твоя толпа цепляет перцев\n" \
          "Я не знаю, почему я ненавижу немцев\n" \
          "Не знаю, кто ты такой, и не хочу знат\n" \
          "Знаю, что очень легко твою жену снять\n" \
          "Я не знаю, почему она такая стерва\n" \
          "Не знаю, почему мой хуй здоровый, как у негра\n" \
          "Я не знаю, почему я не читаю книги\n" \
          "Не знаю, почему ты носишь розовые стринги"

test_text = idk_why

print("source text")
print(test_text)
print()

print("russian - romanian - french - chinese - russian")
print()

result = tr.translate(test_text, src='ru', dest='ro')
result1 = tr.translate(result.text, src='ro', dest='fr')
result2 = tr.translate(result1.text, src='fr', dest='zh-CN')
result3 = tr.translate(result2.text, src='zh-CN', dest='ru')
print(result3.text)
print()

print("russian - japanese - chinese - russian")
print()
result = tr.translate(test_text, src='ru', dest='ja')
result1 = tr.translate(result.text, src='ja', dest='zh-CN')
result2 = tr.translate(result1.text, src='zh-CN', dest='ru')
print(result2.text)
print()

print("russian - poland  - chinese - russian")
print()
result = tr.translate(test_text, src='ru', dest='pl')
result1 = tr.translate(result.text, src='pl', dest='zh-CN')
result2 = tr.translate(result1.text, src='zh-CN', dest='ru')
print(result2.text)
print()

print("russian - tibetan  - chinese - russian")
print()
result = tr.translate(test_text, src='ru', dest='zh-TW')
result1 = tr.translate(result.text, src='zh-TW', dest='zh-CN')
result2 = tr.translate(result1.text, src='zh-CN', dest='ru')
print(result2.text)
print()

print("russian - hungarian - yiddish - chinese - russian")
print()

result = tr.translate(test_text, src='ru', dest='hu')
result1 = tr.translate(result.text, src='hu', dest='yi')
result2 = tr.translate(result1.text, src='yi', dest='zh-CN')
result3 = tr.translate(result2.text, src='zh-CN', dest='ru')
print(result3.text)
print()

print("russian - arabian - portuguese - chinese - russian")
print()

result = tr.translate(test_text, src='ru', dest='ar')
result1 = tr.translate(result.text, src='ar', dest='pt')
result2 = tr.translate(result1.text, src='pt', dest='zh-CN')
result3 = tr.translate(result2.text, src='zh-CN', dest='ru')
print(result3.text)
print()

print("russian - bengali - deutsch - swahili - chinese - russian")
print()

result = tr.translate(test_text, src='ru', dest='bn')
result1 = tr.translate(result.text, src='bn', dest='de')
result2 = tr.translate(result1.text, src='de', dest='sw')
result3 = tr.translate(result2.text, src='sw', dest='zh-CN')
result4 = tr.translate(result3.text, src='zh-CN', dest='ru')
print(result4.text)
print()

print("russian - czech - persian - chinese - russian")
print()

result = tr.translate(test_text, src='ru', dest='cs')
result1 = tr.translate(result.text, src='cs', dest='fa')
result2 = tr.translate(result1.text, src='fa', dest='zh-CN')
result3 = tr.translate(result2.text, src='zh-CN', dest='ru')
print(result3.text)
print()
