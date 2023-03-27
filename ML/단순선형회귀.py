# 방금 막 머신러닝과 관련된 과제를 해결해서 기록할 겸 작성해본다.
# 기존에 존재하는 키와 몸무게 데이터에 대해 학습을 한뒤 사용자에게 키를 입력받아 몸무게를 예측하는 프로그램을 작성할 것이다.

# numpy 를 import 시켜준다.
# numpy 는 선형대수학을 위한 라이브러리이다. 자세한 것은 따로 검색해서 찾아보자.
import numpy as np

# 키와 몸무게에 대한 리스트를 생성한다. 각 리스트 별 인덱스는 서로 관계가 있다.
# 예를 들어 160 cm 인 사람은 50kg 인 것이다.
heights = [160, 165, 170, 175, 180, 185]
weights = [50, 55, 68, 75, 80, 90]

# numpy 를 활용하여 데이터를 다루기 쉽게 해준다.
# 몸무게에 대한 예측을 할 것이기 때문에 y 값은 몸무게가 된다.
x_train = np.array(heights)
y_train = np.array(weights)


# 키의 단위를 m 로 바꿔서 다시 저장한다.
x_train = x_train * 0.01


# 단순선형회귀에서 기본 예측값은 다음과 같다.
# H(x) = W * x + b
# 일차방정식의 느낌이난다. y = ax + b
# 여기서 H(x) 는 예측값이고 W 는 가중치, b 는 편차이다.
# 즉, x 의 자리에 x_train 을 넣어서 잘 학습시키면 어떤 것이 와도 예측값을 알 수 있다는 것이다.
# 우선 가중치와 편차를 초기화해준다.
W = 0.0
b = 0.0



# 학습률을 초기화해준다. 보통 많게는 0.1 에서 적게는 0.001 까지의 값중 하나를 설정해준다.
# 아직 학습률에 대해서는 잘 몰라서 설명을 잘 못하겠다...
learning_rate = 0.01


# 예측값을 구하는 함수이다.
def hypothesis(x):

    # 원래는 예측값을 이렇게 구하는것이 아니지만
    # 귀찮아서 바꿔주었다
    H = W * (x * 0.01) + b
    return H



# 평균제곱오차를 구하는 함수이다.
# 이것의 결과가 낮으면 낮을수록 예측 정확도가 올라가게 된다.
def mse_loss(y_true, hypothesis):
    loss = np.mean((hypothesis - y_true) ** 2)
    return loss



# x 와 y 에 대한 학습값과 가중치, 편차, 학습률, 그리고 에포크(epochs) 를 매개변수로 준다.
# epochs 는 학습을 얼마만큼 시킬거냐에 대한 값이다. 값이 높을수록 많은 학습을 시키게 되고
# 학습에 오랜 시간이 걸리지만 예측 정확도가 비교적 높아진다.
def learning(x_train, y_train, W, b, learning_rate, epochs):
    for epoch in range(epochs):

        # 예측값을 정해준다
        # 코드를 보고 '왜 hypothesis() 를 안썼지?' 라고 생각하는 사람은 직접 써보길 바란다.
        # 해당 부분 때문에 다른 거 다 맞게 했었는데도 밤을 새가며 고쳤다...
        H = W * x_train + b


        # 학습이 얼마나 잘되고 있는지 판단하기 위해 평균제곱오차를 구해준다.
        # y 의 학습값과 미리 구해둔 예측값을 넘겨준다.
        loss = mse_loss(y_train, H)



        # 가중치와 편차를 업데이트 해준다.
        gradient_w = np.mean((H - y_train) * x_train)
        gradient_b = np.mean(H - y_train)
        W = W - learning_rate * gradient_w
        b = b - learning_rate * gradient_b


        # 로그를 출력해서 확인
        if epoch % 1000 == 0 or epoch == epochs-1:
            print('epoch: {}, loss= {:.4f}, W= {:.4f}, b= {:.4f}'.format(epoch, loss, W, b))

    # 학습된 가중치와 편차를 반환
    return W, b


W, b = learning(x_train, y_train, W, b, learning_rate, epochs=200000)
height = int(input('키를 입력하세요: '))
weight = hypothesis(height)

print('예측 몸무게는 {:.4f}kg 입니다.'.format(weight))