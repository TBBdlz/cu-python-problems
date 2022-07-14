using Printf


a = readline()
a = parse(Float64, a)

function mid(lst)
    return (lst[1] + lst[2]) / 2
end

# find approximation of f(a)
function bisec(f::Function, a::Float64)
    L::Float64 = 0.0
    U::Float64 = a
    ans_range = Array([L, U])
    x = mid(ans_range)
    while abs(a - f(x)) > (10^-10 * max(a, f(x)))
        if f(x) > a
            ans_range[2] = x
        elseif f(x) < a
            ans_range[1] = x
        end
        x = mid(ans_range)
    end
    return x
end

approx_val = bisec(log, a)
@printf "log(%d) = %.5f" a approx_val