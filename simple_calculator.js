function add(a, b) {
    try {
        const result = parseFloat(a) + parseFloat(b)
        if (result) {
            return result
        }
        return 'Error, enter number only'
    }
    catch {
        return 'Error, enter number only'
    }
   
}

function subtract(a, b) {
    try {
        const result = parseFloat(a) - parseFloat(b)
        if (result) {
            return result
        }
        return 'Error, enter number only'
    }
    catch {
        return 'Error, enter number only'
    }
}

function multiply(a, b) {
    try {
        const result = parseFloat(a) * parseFloat(b)
        if (result) {
            return result
        }
        return 'Error, enter number only'
    }
    catch {
        return 'Error, enter number only'
    }
}

function divide(a, b) {
    try {
        const result = parseFloat(a) / parseFloat(b)
        if (result) {
            return result
        }
        return 'Error, enter number only'
    }
    catch {
        return 'Error, enter number only'
    }
}

console.log(divide(3.5,5));