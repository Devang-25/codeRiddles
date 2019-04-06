#!/usr/bin/lua

function integers ()
    local count = 0
    return function ()
        while true do
            yield (count)
            count = count + 1
        end
    end
end

function generateInteger ()
    return resume(integers)
end

print (generateInteger())
print (generateInteger())

-- generateInteger() => 0
-- generateInteger() => 1
-- generateInteger() => 2
