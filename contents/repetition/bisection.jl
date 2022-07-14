using Printf
using InverseFunctions

a = readline()
a = parse(Float64, a)

function mid(lst)
    return (lst[1] + lst[2]) / 2
end

# find approximation of f(a)
function bisec(f::Function, a::Float64)
    L::Float64 = 0.0
    U::Float64 = a
    ans_range = Array{Float64}([L, U])
    x = mid(ans_range)
    inv_f::Function = inverse(f)
    # x = f(a) -> f-1(x) = a -> a - f-1(x) near 0 
    while abs(a - inv_f(x)) > (10^-10 * max(a, inv_f(x)))
        if inv_f(x) > a
            ans_range[2] = x
        elseif inv_f(x) < a
            ans_range[1] = x
        end
        x = mid(ans_range)
    end
    return x
end

approx_val = bisec(log, a)
@printf "log(%d) = %.5f" a approx_val