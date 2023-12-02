# app.py
from flask import Flask, render_template, request
import numpy as np
from numpy.linalg import eig

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/matrix_operations', methods=['POST'])
def matrix_operations():
    matrix_a = np.array([[int(request.form[f'A{i}{j}']) for j in range(3)] for i in range(3)])
    matrix_b = np.array([[int(request.form[f'B{i}{j}']) for j in range(3)] for i in range(3)])

    # 行列の足し算
    result_addition = matrix_a + matrix_b

    # 行列の積
    result_multiplication = np.dot(matrix_a, matrix_b)

    return render_template('result.html', result_addition=result_addition, result_multiplication=result_multiplication)

# if __name__ == '__main__':
#    app.run(debug=True)  # この行をコメントアウトまたは削除

@app.route('/eigenvalues', methods=['POST'])
def eigenvalues():
    matrix_a = np.array([[int(request.form[f'A{i}{j}']) for j in range(3)] for i in range(3)])

    # 固有値と固有ベクトルの計算
    eigenvalues, eigenvectors = eig(matrix_a)

    return render_template('eigenvalues.html', eigenvalues=eigenvalues, eigenvectors=eigenvectors)

# 下記の行を追加
if __name__ == '__main__':
    app.run(debug=True)
