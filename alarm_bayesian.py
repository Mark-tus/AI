 pip intsall pgmpy
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
# Create a Bayesian Network
model = BayesianNetwork(
 [('Burglary', 'Alarm'), ('Earthquake', 'Alarm'), ('Alarm', 'Mary'), ('Alarm','John')])

# Define Conditional Probability Distributions (CPDs)
cpd_burglary = TabularCPD(
 variable='Burglary', variable_card=2, values=[[0.999], [0.001]])
cpd_earthquake = TabularCPD(variable='Earthquake',variable_card=2, values=[[0.998],[0.002]])
cpd_alarm = TabularCPD(variable='Alarm', variable_card=2, values=[[0.999,0.71, 0.06, 0.05],[0.001, 0.29, 0.94, 0.95]],evidence=['Burglary', 'Earthquake'], evidence_card=[2, 2])
cpd_mary = TabularCPD(variable='Mary', variable_card=2, values=[[0.95, 0.1],[0.05, 0.9]],evidence=['Alarm'], evidence_card=[2])
cpd_john = TabularCPD(variable='John', variable_card=2, values=[[0.9,0.05],[0.1,0.95]],evidence=['Alarm'],evidence_card=[2])

# Add CPDs to the model
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_mary,cpd_john)

# Check if the model is valid
print(model.check_model())

# Perform inference using Variable Elimination
inference = VariableElimination(model)

# Compute probability of Alarm given evidence
query_result = inference.query(variables=['Alarm'])
print("Probability distribution of Alarm:")
print(query_result)

# Compute probability of Alarm given evidence that Mary heard the alarm
query_result = inference.query(variables=['Alarm'], evidence={'Mary': 1})
print("\nProbability distribution of Alarm given Mary heard the alarm:")
print(query_result)

# Compute probability of Alarm given evidence that John didn't hear the alarm
query_result = inference.query(variables=['Alarm'], evidence={'John': 0})
print("\nProbability distribution of Alarm given John didn't hear the alarm:")
print(query_result)