import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.time_label = QtWidgets.QLabel()
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)

        self.close_button = QtWidgets.QPushButton("Close")
        self.close_button.clicked.connect(self.close)

        self.tabs = QtWidgets.QTabWidget()
        self.text_label = QtWidgets.QLabel("""
Алгоритм скользящего окна - это техника, используемая для оптимизации алгоритмов, которые обрабатывают последовательность данных. 
Он работает путем перемещения "окна" фиксированного размера по последовательности, обрабатывая данные в окне одновременно.

Принцип работы:

    Инициализация: Устанавливается размер окна и устанавливается начальное положение окна в начале последовательности.
    
    Обработка данных в окне: Данные в текущем окне обрабатываются, и выполняется требуемая операция 
    (например, поиск максимального элемента, подсчет уникальных элементов, вычисление суммы).
    
    Перемещение окна: Окно сдвигается на один элемент вправо.
    
    Повторение: Шаги 2-3 повторяются до тех пор, пока окно не достигнет конца последовательности.

Пример алгоритма на задаче из Leetcode:

Задача:
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Далее представлено мое решение на c++


    public:
    static inline array<int, 26> count(string& s, int l, int r) {
        array<int, 26> freq={0};
        for(int i=l; i<=r; i++)
            freq[s[i]-'a']++;
        return freq;
    }
    
    static bool checkInclusion(string& s1, string& s2) {
        const int n1=s1.size(), n2=s2.size();
        if (n2<n1) return 0;
        auto freq1=count(s1, 0, n1-1);
        auto freq2=count(s2, 0, n1-1);
        if (freq1==freq2) return 1;
        for(int l=1, r=n1; r<n2; r++, l++){
            freq2[s2[l-1]-'a']--;
            freq2[s2[r]-'a']++;
            if (freq2== freq1)
        }
        return 0;
    }
};

Опишу алгоритм вкратце:

Функция count(string& s, int l, int r):
    - Эта функция подсчитывает количество каждого символа в строке s между индексами l и r (включительно).
    - Она использует массив freq размера 26 (по количеству букв английского алфавита) для хранения частот.
    - Для каждого символа в строке s она увеличивает соответствующий элемент в freq на 1.
    - В конце она возвращает массив freq с подсчетом частот.

2. Функция checkInclusion(string& s1, string& s2):
    - Эта функция проверяет, является ли строка s1 подстрокой строки s2, независимо от порядка символов.
    - Сначала она проверяет длины строк: если s2 короче s1, то s1 не может быть подстрокой, и функция возвращает false.
    - Далее, она создает два массива freq1 и freq2, используя функцию count(), для подсчета частот символов в s1 и в первых n1 символах s2 (где n1 - длина s1).
    - Если freq1 и freq2 равны, то s1 уже является подстрокой s2 (порядок символов не имеет значения), и функция возвращает true.
    - Если freq1 и freq2 не равны, то функция переходит к итерации по остальным символам s2.
    - В цикле for она перемещает "слайдинг-виндoу" по строке s2 (с помощью l и r).
    - Для каждого шага цикла:
        - Она уменьшает количество символа s2[l-1] в freq2.
        - Она увеличивает количество символа s2[r] в freq2.
        - Она сравнивает freq2 с freq1. Если они равны, то s1 является подстрокой s2 и функция возвращает true.
    - Если цикл завершился, не найдя равных массивов freq1 и freq2, то s1 не является подстрокой s2 и функция возвращает false.

Пример работы:

Представьте, что s1 = "abc" и s2 = "cbca".

1. count(s1, 0, 2) вернет {1, 1, 1}.
2. count(s2, 0, 2) вернет {1, 1, 1}.
3. freq1 и freq2 равны, поэтому функция возвращает true (сразу же).

Если бы s2 был bac, алгоритм прошел бы цикл, сравнивая freq1 и freq2 с каждым сдвигом "слайдинг-виндoу". 

Преимущества этого алгоритма:

- Эффективность: 
Алгоритм работает за линейное время (O(n2)).
- Простота реализации: 
Код легко понять и реализовать.
- Универсальность: 
Алгоритм подходит для проверки наличия любой подстроки в любой строке.

Недостаток:

- Сложность при больших данных:
Для очень длинных строк этот алгоритм может быть медленным, особенно если сравнивать freq1 и freq2 для каждой позиции.
""")
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidget(self.text_label)
        self.scroll_area.setWidgetResizable(True)

        self.tabs.addTab(self.scroll_area, "Text")

        self.video_widget = QVideoWidget()
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)

        tab2_layout = QtWidgets.QVBoxLayout()
        tab2_layout.addWidget(self.video_widget)
        tab2_layout.addWidget(QtWidgets.QPushButton("Play", clicked=self.play_video))
        tab2_layout.addWidget(QtWidgets.QPushButton("Stop", clicked=self.stop_video))
        tab2 = QtWidgets.QWidget()
        tab2.setLayout(tab2_layout)
        self.tabs.addTab(tab2, "Video")

        self.tabs.addTab(QtWidgets.QWidget(), "Audio")

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.close_button)
        self.setLayout(self.layout)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        current_time = QtCore.QTime.currentTime().toString('hh:mm:ss')
        self.time_label.setText(current_time)

    def play_video(self):
        video_url = "content/cat.mp4"
        if os.path.exists(video_url):
            print("1")
            self.media_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(video_url)))
            self.media_player.play()
            if os.access(video_url, os.R_OK):
                print("1")
        else:
            print("Video not found")
            QMessageBox.information(self, "Error", "Video not found")

    def browse_media(self):
        

    def stop_video(self):
        self.media_player.stop()

    def close(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(QtGui.QFont("Jetbrains mono", 10, QtGui.QFont.Bold))
    window = MyWindow()
    window.setWindowTitle("GoidaTube")
    window.resize(1280, 720)
    window.show()
    sys.exit(app.exec_())