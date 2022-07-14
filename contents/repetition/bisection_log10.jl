using Printf


a = readline()
a = parse(Float64, a)

function mid(lst)
    return (lst[1] + lst[2]) / 2
end

# find approximation of log10(a)
function bisec_log10(a::Float64)
    L::Float64 = 0.0
    U::Float64 = a
    ans_range = Array([L, U])
    x = mid(ans_range)
    while abs(a - 10^x) > (10^-10 * max(a, 10^x))
        if 10^x > a
            ans_range[2] = x
        elseif 10^x < a
            ans_range[1] = x
        end
        x = mid(ans_range)
    end
    return x
end

approx_val = bisec_log10(a)
@printf "log10(%d) = %.5f" a approx_val