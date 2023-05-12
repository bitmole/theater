# https://github.com/dabeaz/theater
#
# The owner of a monopolistic movie theater in a small town has
# complete freedom in setting ticket prices.  The more he charges, the
# fewer people can afford tickets.  The less he charges, the more it
# costs to run a show because attendance goes up.  In a recent
# experiment the owner determined a relationship between the price of
# a ticket and average attendance.
#
# At a price of $5.00/ticket, 120 people attend a performance.  For
# each 10-cent change in the ticket price, the average attendance
# changes by 15 people.  That is, if the owner charges $5.10, some 105
# people attend on the average; if the price goes down to $4.90,
# average attendance increases to 135.
#
# Unfortunately, the increased attendance also comes at an increased
# cost.  Every performance comes at a fixed cost of $180 to the owner
# plus a variable cost of $0.04 per attendee.
#
# The owner would like to know the exact relationship between profit
# and ticket price in order to maximize the profit.
#
# Write a program to figure out the best ticket price (to the nearest
# 10 cents) that maximizes profit.
#
# Credit: This problem comes from "How to Design Programs", 2nd Ed.
# by Felleisen, Findler, Flatt, and Krishnamurthi.  pg. 60.


def attendance_at(price):
    """
    Calculates number of attendees at given price
    """
    return 120 + diff_attendance(price)

def diff_attendance(price):
    """Calculates difference in attendence at given price
        according to following function:

        diff_price      | 10 | 20 | 30 | 40
        diff_attendance | 15 | 30 | 45 | 60
        
        This denotes linear f(x) = 1.5.x
                            f(x) = 3/2 x
                            f(x) = (3 * x) / 2

    :price: ticket price
    :returns: difference in attendance as compared to attendance at base price

    """
    return (3 * diff_price(price)) // 2

def diff_price(price):
    """
    Calculates difference between base price ($5.00) and given price

    :price: ticket price
    :returns: price difference *in cents*
    """
    diff_cents = round(price * 100)
    return 500 - diff_cents

assert attendance_at(5.00) == 120
assert attendance_at(5.10) == 105
assert attendance_at(4.90) == 135
