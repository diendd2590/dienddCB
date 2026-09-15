## Đây là bài reverse đầu tiên mà mình làm nên sẽ viết kĩ chút 

Thì khi chúng ta tải file chương trình cho về nó là một file code python ntn
```python
import re
import time

# Read in flag from file
flag = open('flag.txt', 'r').read()

secret_intro = \
'''Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether’s ours to conquer, '''\
+ flag + '\n'

song_flag_hunters = secret_intro +\
'''

[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
CROWD (Singalong here!);
RETURN

[VERSE1]
Command line wizards, we’re starting it right,
Spawning shells in the terminal, hacking all night.
Scripts and searches, grep through the void,
Every keystroke, we're a cypher's envoy.
Brute force the lock or craft that regex,
Flag on the horizon, what challenge is next?

REFRAIN;

Echoes in memory, packets in trace,
Digging through the remnants to uncover with haste.
Hex and headers, carving out clues,
Resurrect the hidden, it's forensics we choose.
Disk dumps and packet dumps, follow the trail,
Buried deep in the noise, but we will prevail.

REFRAIN;

Binary sorcerers, let’s tear it apart,
Disassemble the code to reveal the dark heart.
From opcode to logic, tracing each line,
Emulate and break it, this key will be mine.
Debugging the maze, and I see through the deceit,
Patch it up right, and watch the lock release.

REFRAIN;

Ciphertext tumbling, breaking the spin,
Feistel or AES, we’re destined to win.
Frequency, padding, primes on the run,
Vigenère, RSA, cracking them for fun.
Shift the letters, matrices fall,
Decrypt that flag and hear the ether call.

REFRAIN;

SQL injection, XSS flow,
Map the backend out, let the database show.
Inspecting each cookie, fiddler in the fight,
Capturing requests, push the payload just right.
HTML's secrets, backdoors unlocked,
In the world wide labyrinth, we’re never lost.

REFRAIN;

Stack's overflowing, breaking the chain,
ROP gadget wizardry, ride it to fame.
Heap spray in silence, memory's plight,
Race the condition, crash it just right.
Shellcode ready, smashing the frame,
Control the instruction, flags call my name.

REFRAIN;

END;
'''

MAX_LINES = 100

def reader(song, startLabel):
    lip = 0
    start = 0
    refrain = 0
    refrain_return = 0
    finished = False

    # Get list of lyric lines
    song_lines = song.splitlines()
    
    # Find startLabel, refrain and refrain return
    for i in range(0, len(song_lines)):
        if song_lines[i] == startLabel:
            start = i + 1
        elif song_lines[i] == '[REFRAIN]':
            refrain = i + 1
        elif song_lines[i] == 'RETURN':
            refrain_return = i

    # Print lyrics
    line_count = 0
    lip = start
    while not finished and line_count < MAX_LINES:
        line_count += 1
        for line in song_lines[lip].split(';'):
            if line == '' and song_lines[lip] != '':
                continue
            if line == 'REFRAIN':
                song_lines[refrain_return] = 'RETURN ' + str(lip + 1)
                lip = refrain
            elif re.match(r"CROWD.*", line):
                crowd = input('Crowd: ')
                song_lines[lip] = 'Crowd: ' + crowd
                lip += 1
            elif re.match(r"RETURN [0-9]+", line):
                lip = int(line.split()[1])
            elif line == 'END':
                finished = True
            else:
                print(line, flush=True)
                time.sleep(0.5)
                lip += 1

reader(song_flag_hunters, '[VERSE1]')
```
Về cơ bản thì đây là code để in ra lời của một bài hát khi chúng ta chạy trực tiếp nó thông quá netcat 
Khi đọc qua ta có thể thấy là flag đang được giấu trong flag.txt mà chúng ta chưa cò file đấy nên phải lợi dụng code để lấy ra t
thông qua netcat
Ở đây bài hát này sẽ đc chia ra theo dòng có một đoạn 'REFRAINT' ở trên cùng để lặp lại đoạn đấy sau mỗi đoạn thường khi đọc phần code
in ta thấy ns ko check dữ liệu người dùng nhập vào phần crowd và lại có lệnh tách mỗi dòng khi có kí tự ';' vậy nếu chúng ta nhập
';RETURN 0' nó sẽ tách xuống dòng return 0 ngay lập tức và khi đọc đến dòng này ns sẽ ép cái lib từ i thành 0 và in ra mấy dòng đầu

<img width="452" height="430" alt="Screenshot 2026-09-15 215934" src="https://github.com/user-attachments/assets/211641e8-de28-4c0d-80bf-15c31bd6af00" />
ta có thể thấy khi đã đọc được lệnh ta nhập vào ns sẽ chỉ spam đi spam lại refrain và đoạn secret vì lib bị kẹt r
