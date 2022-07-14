using Printf


a = readline()
a = parse(Float64, a)

function mid(lst)
    return (lst[1] + lst[2]) / 2
end

x = [1, 2, 3]
# find approximation of sqrt(a)
function bisec_sqrt(a)
    L = 0
    U = a
    ans_range = Array([L, U])
    x = mid(ans_range)
    while abs(a - x^2) > (10^-10 * max(a, x^2))
        x = mid(ans_range)
        if x^2 > a
            ans_range[2] = x
        elseif x^2 < a
            ans_range[1] = x
        end
        x = mid(ans_range)
    end
    return x
end

approx_val = bisec_sqrt(a)
@printf "sqrt(%d) = %.5f" a approx_val