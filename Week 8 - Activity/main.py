"""
CityBikeGo
"""


# =========================
# Phase 1 – Setup and Data
# =========================

def loadSampleData():
    """
    Create and return sample data structures for the task.

    Returns
    -------
    tuple :
        customerMonthOne : list of str
        customerMonthTwo : list of str
        bookingData : list of tuples (customerId, stationName, dayType, durationHours)
        loyalCustomerSet : set of str
    """
    customerMonthOne = [
        "Ali", "Ben", "Ali", "Dana", "Cara", "Ben"
    ]

    customerMonthTwo = [
        "Ali", "Ella", "Ben", "Frank", "Cara", "Ben"
    ]

    bookingData = [
        ("Ali", "StationA", "Weekday", 2),
        ("Ben", "StationB", "Weekend", 1),
        ("Ali", "StationA", "Weekday", 3),
        ("Cara", "StationC", "Weekday", 2),
        ("Ella", "StationB", "Weekend", 2)
    ]

    loyalCustomerSet = {"Ali", "Cara"}

    return customerMonthOne, customerMonthTwo, bookingData, loyalCustomerSet


# =================================
# Phase 2 – Sets for Customer Analysis
# =================================

def buildCustomerSets(customerMonthOne, customerMonthTwo):
    """
    Convert raw customer lists into sets to remove duplicates.

    Parameters
    ----------
    customerMonthOne : list of str
    customerMonthTwo : list of str

    Returns
    -------
    tuple :
        setMonthOne : set of str
        setMonthTwo : set of str
    """
    # TODO:
    # 1. Convert each list to a set (list to set).
    # 2. Optionally show conversion back to list or tuple.
    setMonthOne = set(customerMonthOne)
    setMonthTwo = set(customerMonthTwo)

    return setMonthOne, setMonthTwo


def analyseCustomerActivity(setMonthOne, setMonthTwo):
    """
    Use set operations to classify customers.

    Parameters
    ----------
    setMonthOne : set of str
    setMonthTwo : set of str

    Returns
    -------
    tuple :
        regularCustomers : set of str
        newCustomers : set of str
        inactiveCustomers : set of str
        allUniqueCustomers : set of str
    """
    # TODO:
    # Use:
    #   union to get allUniqueCustomers
    #   intersection for regularCustomers
    #   difference for newCustomers and inactiveCustomers
    # Also consider issubset, issuperset, isdisjoint if relevant.
    regularCustomers = setMonthOne.intersection(setMonthTwo)
    newCustomers = setMonthTwo.difference(setMonthOne)
    inactiveCustomers = setMonthOne.difference(setMonthTwo)
    allUniqueCustomers = setMonthOne.union(setMonthTwo)

    return regularCustomers, newCustomers, inactiveCustomers, allUniqueCustomers


# =====================================
# Phase 3 – Tuples for Booking Records
# =====================================

def showBookingTupleUsage(bookingData):
    """
    Demonstrate tuple indexing, unpacking, and simple operations.

    Parameters
    ----------
    bookingData : list of tuples
        Each tuple: (customerId, stationName, dayType, durationHours)

    Returns
    -------
    None
    """
    # Example of unpacking the first booking
    if bookingData:
        firstBooking = bookingData[0]
        # Tuple indexing
        firstCustomer = firstBooking[0]
        firstStation = firstBooking[1]
        # Tuple unpacking
        customerId, stationName, dayType, durationHours = firstBooking

        print("Example booking tuple:", firstBooking)
        print("First booking customer:", firstCustomer)
        print("First booking station:", firstStation)
        print("Unpacked booking:", customerId, stationName, dayType, durationHours)

    


# =====================================
# Phase 4 – Dictionaries for Aggregation
# =====================================

def buildStationStats(bookingData):
    """
    Build a dictionary storing station activity counts.

    Parameters
    ----------
    bookingData : list of tuples
        Each tuple: (customerId, stationName, dayType, durationHours)

    Returns
    -------
    dict :
        stationCounts : dict mapping stationName (str) to number of bookings (int)
        stationCustomerSet : dict mapping stationName (str) to set of customers (set of str)
    """
    stationCounts = {}
    stationCustomerSet = {}

    for booking in bookingData:
        customerId, stationName, dayType, durationHours = booking

   
        currentCount = stationCounts.get(stationName, 0)
        stationCounts[stationName] = currentCount + 1

        # Use setdefault for stationCustomerSet
        customerSetForStation = stationCustomerSet.setdefault(stationName, set())
        customerSetForStation.add(customerId)

 
    return stationCounts, stationCustomerSet


def buildCustomerStats(bookingData):
    """
    Build a dictionary mapping each customer to total hours cycled.

    Parameters
    ----------
    bookingData : list of tuples
        Each tuple: (customerId, stationName, dayType, durationHours)

    Returns
    -------
    dict :
        customerHours : dict mapping customerId (str) to total durationHours (float or int)
    """
    customerHours = {}

    for booking in bookingData:
        customerId, stationName, dayType, durationHours = booking

      
        currentHours = customerHours.get(customerId, 0)
        customerHours[customerId] = currentHours + durationHours

    # TODO:
    # Demonstrate other dictionary methods somewhere in the script:
    #   update
    #   pop
    #   popitem
    #   clear
    #   copy
    #   fromkeys
    #
    # For example, you might create:
    # tempCopy = customerHours.copy()
    # dummyDict = dict.fromkeys(customerHours.keys(), 0)
    return customerHours


def findBusiestStation(stationCounts):
    """
    Find the station with the highest number of bookings.

    Parameters
    ----------
    stationCounts : dict
        Keys: stationName (str), Values: booking count (int)

    Returns
    -------
    tuple :
        busiestStationName : str
        busiestStationCount : int
    """
    if not stationCounts:
        return None, 0

    # Simple max by value
    #Google the following statement to see what it means and does
    busiestStationName = max(stationCounts, key=lambda name: stationCounts[name])
    busiestStationCount = stationCounts[busiestStationName]

    return busiestStationName, busiestStationCount


# =================================
# Phase 5 – Report Generation
# =================================

def generateSummaryReport(
    regularCustomers,
    newCustomers,
    inactiveCustomers,
    allUniqueCustomers,
    stationCounts,
    stationCustomerSet,
    busiestStationName,
    busiestStationCount,
    customerHours,
):
    """
    Print a readable summary report for CityBikeGo.

    Parameters
    ----------
    regularCustomers : set of str
    newCustomers : set of str
    inactiveCustomers : set of str
    allUniqueCustomers : set of str
    stationCounts : dict mapping stationName to booking count
    stationCustomerSet : dict mapping stationName to set of customers
    busiestStationName : str
    busiestStationCount : int
    customerHours : dict mapping customerId to total hours

    Returns
    -------
    None
    """
    print("\n=== CityBikeGo Monthly Summary Report ===\n")

    print("Total unique customers this month:", len(allUniqueCustomers))
    print("Regular customers (both months):", sorted(regularCustomers))
    print("New customers (this month only):", sorted(newCustomers))
    print("Inactive customers (did not return):", sorted(inactiveCustomers))
    print()

    print("Station activity (bookings per station):")
    for stationName, count in stationCounts.items():
        print(f"  {stationName}: {count} bookings, {len(stationCustomerSet[stationName])} customers")

    print()
    print("Busiest station:", busiestStationName, "with", busiestStationCount, "bookings")
    print()

    print("Customer hours cycled:")
    for customerId, hours in customerHours.items():
        print(f"  {customerId}: {hours} hours")

    print("\n=== End of Report ===\n")


# =================================
# Phase 6 – Reflection (for report)
# =================================

def printReflectionHints():
    """
    Print prompts for the reflection section (to be answered in a separate report or comment block).

    Returns
    -------
    None
    """
    print("Reflection prompts:")
    print("- Why were sets essential for customer analysis?")
    print("- Why choose tuples for booking records?")
    print("- Why do dictionaries suit station and customer statistics?")
    print("- Which methods (get, setdefault, update, pop, etc.) did you use and why?")
    print()


# =================================
# Main Orchestration
# =================================

def runCityBikeGoAnalysis():
    """
    High-level orchestration function.

    Steps:
    1. Load or define sample data.
    2. Build and analyse customer sets.
    3. Work with booking tuples.
    4. Build dictionaries for station and customer statistics.
    5. Generate a final summary report.
    6. Print reflection hints for the written summary.
    """
    # Phase 1 – Setup
    customerMonthOne, customerMonthTwo, bookingData, loyalCustomerSet = loadSampleData()

    # Phase 2 – Sets for Customer Analysis
    setMonthOne, setMonthTwo = buildCustomerSets(customerMonthOne, customerMonthTwo)
    regularCustomers, newCustomers, inactiveCustomers, allUniqueCustomers = analyseCustomerActivity(
        setMonthOne, setMonthTwo
    )

    # Phase 3 – Tuples for Booking Records
    showBookingTupleUsage(bookingData)

    # Phase 4 – Dictionaries for Aggregation
    stationCounts, stationCustomerSet = buildStationStats(bookingData)
    customerHours = buildCustomerStats(bookingData)
    busiestStationName, busiestStationCount = findBusiestStation(stationCounts)

    # Phase 5 – Report Generation
    generateSummaryReport(
        regularCustomers,
        newCustomers,
        inactiveCustomers,
        allUniqueCustomers,
        stationCounts,
        stationCustomerSet,
        busiestStationName,
        busiestStationCount,
        customerHours,
    )

    # Phase 6 – Reflection
    printReflectionHints()


if __name__ == "__main__":
    runCityBikeGoAnalysis()

""" Challenege Me Optional
Edit your code to conclude the functions below for data visualisation
These functions have to be called somewhere in runCityBikeGoAnalysis()
Think of where to define them
Do not forget to import the required libraries where applicable
# =================================
# Visualisations
# =================================

def plotStationActivity(stationCounts):
    """
    #Bar chart of number of bookings per station.
    #TO Do

    #stationCounts : dict
        #Keys: station names (str)
        #Values: booking counts (int)
    #Complete the rest


def plotCustomerTypes(regularCustomers, newCustomers, inactiveCustomers):
    """
    Bar chart for counts of new, regular, and inactive customers.
    """
    categories = ["Regular", "New", "Inactive"]
    positions = range(len(categories))

    #To Do

    plt.figure()
    plt.tight_layout()
    plt.show()


def plotCustomerHours(customerHours):
    """
    Bar chart showing total hours cycled per customer.

    To Do


    plt.show()


"""
