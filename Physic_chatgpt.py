import nltk
from nltk.tokenize import word_tokenize
import re

def similarity_score(tokens1, tokens2):
    set1 = set(tokens1)
    set2 = set(tokens2)
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    score = intersection / union
    
    return score

physics_info = [
    {
        "topic": "kinematics",
        "equations": ["v = d/t", "a = (v_f - v_i)/t"],
        "description": "Kinematics is the branch of mechanics that deals with the motion of objects without considering the forces that cause the motion."
    },
    {
        "topic": "newton laws",
        "equations": ["F = ma", "F_net = ma"],
        "description": "Newton's laws of motion are three fundamental laws that describe the relationship between the motion of an object and the forces acting upon it."
    },
    {
        "topic": "work and energy",
        "equations": ["W = Fd", "KE = 1/2mv^2"],
        "description": "Work and energy are closely related concepts in physics that describe the ability of a system to do work."
    },
    {
        "topic": "momentum",
        "equations": ["p = mv", "F_net = Δp/Δt"],
        "description": "Momentum is a measure of an object's motion. It is defined as the product of an object's mass and velocity."
    },
    {
        "topic": "gravity",
        "equations": ["F = Gm1m2/r^2", "g = Gm/r^2"],
        "description": "Gravitation is the force of attraction between any two objects in the universe."
    },
    {
        "topic": "circular motion",
        "equations": ["a = v^2/r", "F_c = mv^2/r"],
        "description": "Circular motion is the motion of an object in a circular path at a constant speed."
    },
    {
        "topic": "waves",
        "equations": ["v = λf", "c = λf"],
        "description": "Waves are disturbances that travel through a medium or vacuum."
    },
    {
        "topic": "optics",
        "equations": ["n1sinθ1 = n2sinθ2", "f = 1/p"],
        "description": "Optics is the study of the behavior and properties of light, including its interactions with matter and the instruments used to detect it."
    },
    {
        "topic": "electrostatics",
        "equations": ["F = kq1q2/r^2", "V = kq/r"],
        "description": "Electrostatics is the study of electric charges at rest."
    },
    {
        "topic": "magnetism",
        "equations": ["F = qvB", "B = μ0I/2πr"],
        "description": "Magnetism is a phenomenon that arises from the force between electrically charged particles and the motion of those particles."
    },
    {
        "topic": "electric circuits",
        "equations": ["V = IR", "P = IV", "V = ΔE/q"],
        "description": "Electric circuits are systems that allow the flow of electric current through wires and components."
    },
    {
        "topic": "quantum mechanics",
        "equations": ["E = hf", "ΔxΔp ≥ h/4π"],
        "description": "Quantum mechanics is a branch of physics that deals with the behavior of matter and energy at the atomic and subatomic level."
    },
    {
        "topic": "thermodynamics",
        "equations": ["Q = mcΔT", "ΔS = Q/T", "W = -PΔV"],
        "description": "Thermodynamics is the branch of physics that deals with the relationship between heat, work, and energy in a system."
    },
    {
        "topic": "fluid mechanics",
        "equations": ["ρ = m/V", "P = F/A", "Bernoulli's equation"],
        "description": "Fluid mechanics is the study of how fluids behave when they are in motion or at rest."
    },
    {
        "topic": "nuclear physics",
        "equations": ["E = mc^2", "N = N_0 e^(-λt)", "Q = mΔH"],
        "description": "Nuclear physics is the study of the behavior of atomic nuclei and their interactions with other particles."
    },
    {
        "topic": "special relativity",
        "equations": ["E^2 = (mc^2)^2 + (pc)^2", "Δt' = γΔt", "Δx' = γΔx"],
        "description": "Special relativity is the branch of physics that deals with the behavior of objects moving at high speeds."
    },
    {
        "topic": "general relativity",
        "equations": ["Gμν + Λgμν = 8πTμν", "Rμν - 1/2gμνR = 8πTμν"],
        "description": "General relativity is the theory of gravitation developed by Albert Einstein that explains gravity as the curvature of spacetime caused by mass and energy."
    },
    {
        "topic": "solid state physics",
        "equations": ["E = ℏω", "ρ = m/NV", "F = -dU/dx"],
        "description": "Solid state physics is the study of the behavior of solid materials, particularly their electronic, magnetic, and structural properties."
    },
    {
        "topic": "astrophysics",
        "equations": ["F = GMm/r^2", "L = σAT^4", "E = hf"],
        "description": "Astrophysics is the branch of physics that deals with the behavior and properties of astronomical objects such as stars, galaxies, and black holes."
    },
    {
        "topic": "particle physics",
        "equations": ["E = hf", "E = mc^2", "F = q(E + v × B)"],
        "description": "Particle physics is the study of the fundamental particles and forces that make up the universe."
    },
    {
        "topic": "condensed matter physics",
        "equations": ["E = ℏω", "n = N/V", "F = -dU/dx"],
        "description": "Condensed matter physics is the study of the physical properties of condensed phases of matter, such as solids and liquids."
    },
    {
        "topic": "acoustics",
        "equations": ["v = fλ", "I = P/A", "L = 10 log(I/I_0)"],
        "description": "Acoustics is the study of the properties of sound, including its generation, transmission, and reception."
    }
]


while True:
    def answer_question(question):
        tokens = word_tokenize(question.lower())

        matching_topics = []
        for info in physics_info:
            pattern = re.compile(r"^" + re.escape(" ".join(tokens[2:])))
            if any(pattern.match(token.lower()) for token in word_tokenize(info['topic'])):
                matching_topics.append(info)

        if not matching_topics:
            return "Invalid input"

        best_match = max(matching_topics, key=lambda x: similarity_score(tokens, word_tokenize("what is " + x['topic'].lower())))

        response = best_match['description'] + "\nEquations: " + ", ".join(best_match['equations'])

        return response

    question = input("notes: ")
    answer = answer_question(question)
    print(answer)
