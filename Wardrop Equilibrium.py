#This code calculates the Wardrop Equilibrium for Capacity Constraint

def wardrop_equilibrium(FreeFlowc1, cap1, FreeFlowc2, cap2, demand):
  def link_cost(FreeFlowCost, x, cap):
    return FreeFlowCost * (1 + (x/cap))

  x = demand / 2
  y = demand - x

  while True:
    cost1 = link_cost(FreeFlowc1, x, cap1)
    cost2 = link_cost(FreeFlowc2, y, cap2)

    if abs(cost1 - cost2) < 0.01:    # This the equilibrium equation by equating cost 1 to cost 2
      break

    if cost1 < cost2:
      x += 1
      y -= 1
    else:
      x -= 1
      y += 1

  return x, y, cost1, cost2

FreeFlowc1 = 27
cap1 = 900
FreeFlowc2 = 32
cap2 = 1300
demand = 150

x, y, cost1, cost2 = wardrop_equilibrium(FreeFlowc1, cap1, FreeFlowc2, cap2, demand)

print("Demand on route 1:", round(x, 1))
print("Demand on route 2:", round(y, 1))
print("Travel cost between O-D pair:", round(cost1, 2))

