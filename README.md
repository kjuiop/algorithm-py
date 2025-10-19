# algorithm-py


### f-string (formatted string literal)

파이썬에서 문자열 안에 변수를 간단하고 직관적으로 삽입하는 방법

    ```python
    name = "Sayali"
    age = 29
    print(f"My name is {name} and I am {age} years old.")
    ```


<br />

### enumerate()

파이썬에서 리스트를 순회할 때 인덱스(index) 와 값(value) 를 동시에 얻을 수 있게 해주는 내장함수


  	```python
	for i, v in enumerate(리스트):
    ...

	```

<br />


### range 사용법

```python
range(stop)
range(start, stop)
range(start, stop, step)
```


<br />

### swapcase()

swapcase() 는 문자열의 대문자는 소문자로, 소문자는 대문자로 변경됨

```python
s = "aBcDeFg"
print(s.swapcase())
```


<br />

### 타입 변경

- int : int(a)
- string : str(a)

<br />


### join

'구분자'.join(문자열리스트)


```python
words = ["apple", "banana", "cherry"]
result = "-".join(words)
print(result)
```