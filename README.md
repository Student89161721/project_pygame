# Проект pygame «Сборник игр»
### Авторы: Дарья Рязанова, Полина Федулеева
## Описание проекта
#### При запуске открывается меню с регистрацией и выбором игры. Планируется сделать 3 игры: виселица, дурак и пасьянс косынка
- ### Виселица
#### Один участник (водящий) загадывает слово и рисует на листе такое количество подчёркиваний, сколько букв в слове. Другой участник начинает называть буквы, чтобы отгадать слово. В данном случае загадывающий - бот, будет выбирать слово из базы данных (можно реализовать несколько уровней сложности и для них разные слова) после 6 ошибок игрок проигрывает (если делаем уровни сложности, то число можно менять в зависимости от уровня сложности).
- ### Дурак
#### Правила дурака слишком длинные. Нужно реализовать выбор количества игроков, количества карт в колоде при двойном клике или перетягивании карты на поле она выкладывается есть много договорённостей, которые можно реализовать(ничья, переводной, подкидной и тд), выбор дизайна карт.
- ### Косынка
#### Играется одной колодой в 52 карты. Цель игры — разложить карты по мастям в порядке от туза до короля в четыре стопки (их иногда называют базовыми, или «домами»). Карту можно перекладывать на другую рангом выше, но другого цвета (чёрного или красного). В каждую из четырёх базовых стопок (домов), по которым необходимо разложить все карты, сначала кладутся тузы, затем двойки, тройки и так далее до короля. Карты можно сдавать из оставшейся от раздачи колоды (в левом верхнем углу) либо по одной, либо по три штуки, в зависимости от модификации. В свободную ячейку (не дом) можно положить только короля. Игра заканчивается, когда все карты разложены. Тоже можно реализовать уровни сложности или выбор дизайна карт.