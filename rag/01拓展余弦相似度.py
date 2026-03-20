import math


def get_dot(vec_a, vec_b):
    """计算2个向量的点积， 2个向量同维度数字乘积之和"""
    if len(vec_a) != len(vec_b):
        raise ValueError("两个向量维度不一致")
    dot_sum = 0
    for a,b in zip(vec_a, vec_b):
        dot_sum += a * b
    return dot_sum


def get_norm(vec):
    """计算向量的模长，对向量的每个数字求平方再开根号"""
    sum_square = 0
    for v in vec:
        sum_square += v * v

    return math.sqrt(sum_square)


def get_similarity(vec_a, vec_b):
    """计算两个向量的相似度"""
    dot = get_dot(vec_a, vec_b)
    norm_a = get_norm(vec_a)
    norm_b = get_norm(vec_b)
    return dot / (norm_a * norm_b)


if __name__ == '__main__':
    vec_a = [0.5, 0.5]
    vec_b = [0.7, 0.7]
    vec_c = [0.7, 0.5]
    vec_d = [-0.5, -0.7]
    print("a和b的向量相似度:", get_similarity(vec_a, vec_b))
    print("a和c的向量相似度:", get_similarity(vec_a, vec_c))
    print("a和d的向量相似度:", get_similarity(vec_a, vec_d))
