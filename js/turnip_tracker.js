function fill_array() {
    let my_array = [];
    let prices = document.getElementsByClassName("prices");
    for(let i = 0; i < prices.length; i++) {
        my_array[i] = parseInt(prices[i].value);
    }

    return my_array;
}

function is_decreasing(prev, curr) {
    if((prev > curr) || (!prev)){
        return true;
    }
    return false;
}

function sell_at(pattern, number) {
    let message = ("It is " + pattern + " sell at " + number);
    document.getElementById("pattern").innerHTML = message;
    console.log(message);
}

function pattern_checker() {
    let my_arr = fill_array();
    let decreasing = true;
    let decreasing_pattern = true;
    let random_pattern = false;

    let consecutive_increase = 0;

    let pattern_name = "uknown";
    let sell_price = 0;

    for(let i = 0; i < my_arr.length; i++) {
        decreasing = is_decreasing(my_arr[i-1], my_arr[i]);

        // checking which patterns are active
        if(decreasing === false) {
            decreasing_pattern = false;
        }
        if(consecutive_increase && decreasing === true) {
            random_pattern = true;
        }


        if(decreasing_pattern) {
            if(i === 7) {
                pattern_name = "decreasing";
                sell_price = my_arr[i];
                break;
            }
        }
        else if(random_pattern) {
            if (my_arr[i] >= 110) {
                pattern_name = "random";
                sell_price = my_arr[i];
                break;
            }
        }
        else if(decreasing === false) {
            consecutive_increase++;
            if(consecutive_increase === 3 && my_arr[i] >= 250) {
                pattern_name = "big spike";
                sell_price = my_arr[i];
                break;
            }
            if(consecutive_increase === 4) {
                pattern_name = "small spike";
                sell_price = my_arr[i];
                break;
            }
        }
    }

    sell_at(pattern_name, sell_price);
}