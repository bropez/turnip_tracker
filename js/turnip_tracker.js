function fill_array(my_array) {
    let prices = document.getElementsByClassName("prices");
    for(let i = 0; i < prices.length; i++) {
        my_array[i] = prices[i].value;
    }

    return my_array;
}

function check_for_decrease(prev, curr) {
    if((prev > curr) || (!prev)){
        return true;
    }
    return false;
}

function sell_at(pattern, number) {
    let message = ("It is " + pattern + " sell at " + number);
    document.getElementById("pattern").innerHTML = message;
}

function pattern_checker() {
    let decrease = true;
    let increase_count = 0;
    let all_prices = new Array(10);

    all_prices = fill_array(all_prices)

    for (let i = 0; i < all_prices.length; i++) {

        if (decrease && increase_count) {
            if (all_prices[i] >= 110) {
                sell_at("random", all_prices[i]);
                return all_prices[i];
            }
        }

        decrease = check_for_decrease(all_prices[i - 1], all_prices[i]);

        if (decrease === false) {
            increase_count++;
            if ((increase_count === 3) && (all_prices[i] >= 250)) {
                sell_at("big spike", all_prices[i]);
                return all_prices[i];
            }
            if (increase_count === 4) {
                sell_at("small spike", all_prices[i]);
                return all_prices[i];
            }
        }
    }
}