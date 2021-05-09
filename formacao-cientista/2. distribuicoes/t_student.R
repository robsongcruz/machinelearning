# T de student

# media_salrio=75; amostra=9; dp=10
# p(salario<80)=? ; t=1,5 (calculado); t=(media_amostra - media)/(S / sqrt(n))
# p/ t = 1.5, P ~ 92.5%

media_salario = 75
n_amostras = 9
dp = 10

graus_liberdade = n_amostras - 1
prob = pt(1.5, 8)
prob

# p(salario>=80)=?
prob1 = 1 - prob # ou pt(1.5, 8, lower.tail=F)
prob1