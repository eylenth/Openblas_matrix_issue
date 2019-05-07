load("data.RData")
print(sessionInfo())

n1 <- Khat %*% Khat
n2 <- Khat %*% Khat
print(all.equal(n1, n2))
