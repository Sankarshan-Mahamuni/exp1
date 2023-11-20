import streamlit as st

# Title
st.title("To determine the total hardness of a given water sample")

# First concept
st.subheader("Prior Concept:")
st.write("Hard water, effect of hard water, hardness causing agents.")

# Second concept
st.subheader("New Concepts:")
st.write("Complex formation, EDTA, EBT, Ligand")

st.subheader("Proposition1:")
st.write("Hardness of water is due to the presence of Ca and Mg salts in it.")



import streamlit as st
from PIL import Image

# Open an image file
img_path = r"C:\Users\asu65\Downloads\attachments\Screenshot_20231114-100244_Drive.jpg"
img = Image.open(img_path)



# Display the image using Streamlit
st.image(img,  use_column_width=True)


st.subheader("Proposition 2:")
st.write("(Disodium salt of ethylene diamine tetra acetic acid) is used for determination of hardness by virtue of its stability and its complex forming efficiency with Ca2+ and Mg2+ from hard water. EBT (Eriochrome black-T) is used as an indicator in above complexometric titration. EBT forms wine red complex with Ca/Mg ions. Addition of EDTA displaces these ions and formation of colorless EDTA-M complex with regeneration of blue colored dye takes place. This change in color from red to blue marks the end point of titration.")


import streamlit as st
from PIL import Image

# Open an image file

# Open an image file
img_path = r"C:\Users\asu65\Downloads\attachments\Screenshot_20231114-100321_Drive.jpg"
img = Image.open(img_path)
img = Image.open(img_path)
# Display the image using Streamlit
st.image(img,  use_column_width=True)


st.subheader("Proposition 3:")
st.write("From the amount (ml) of standard solution of disodium-EDTA required during complexometric titration with hard water, the amount of hardness present in hard water sample (in ppm) is calculated.")


import streamlit as st
from PIL import Image



# Open an image file
img_path = r"C:\Users\asu65\Downloads\attachments\Screenshot_20231114-100402_Drive.jpg"
img = Image.open(img_path)

# Display the image using Streamlit
st.image(img,  use_column_width=True)


st.header("Information Input:")
st.subheader("1)Chemical Reactions")

import streamlit as st
from PIL import Image



# Open an image file
img_path = r"C:\Users\asu65\Downloads\attachments\Screenshot_20231114-100424_Drive.jpg"
img = Image.open(img_path)

# Display the image using Streamlit
st.image(img,  use_column_width=True)


st.subheader("2)Structure of Metal-EDTA Complex:")

import streamlit as st
from PIL import Image



# Open an image file
img_path = r"C:\Users\asu65\Downloads\download.png"
img = Image.open(img_path)

# Display the image using Streamlit
st.image(img,  use_column_width=True)



# Chemicals
st.subheader("Chemicals:")
st.write("EDTA, Eriochrome black T, ZnSO4, hard water sample.")

# Apparatus
st.subheader("Apparatus:")
st.write("Burette, pipette, conical flask, etc")

# Stepwise Procedure
st.header("Stepwise Procedure:")
st.subheader("Part I - Standardization of EDTA solution")
st.write("Rinse and fill the burette with a little quantity of EDTA and fill it up to the mark. "
         "Pipette out 10ml ZnSO4 solution and add into it 5 ml of buffer solution having pH 10. "
         "Add 4-5 drops of Eriochrome black T indicator. Titrate this solution against EDTA till "
         "the color changes to sky blue. Repeat the procedure for three times until constant readings "
         "are obtained and find out the molarity of the EDTA solution (M2).")

# NEXT Button
st.subheader("Part II - Determination of total hardness in water:")
st.write("Fill the burette with EDTA solution up to the mark. Pipette out 10ml of water sample "
         "and add to it 5 ml of buffer solution having pH 10. Add 3-4 drops of Eriochrome black T indicator. "
         "Titrate this solution against EDTA till wine red color changes to sky blue. Repeat the procedure "
         "for three times until constant readings are obtained and find out the hardness of the water sample.")

# Observations
st.header("Observations:")
st.subheader("Estimation of total hardness")
st.write("1) In burette - EDTA Solution\n"
         "2) In conical flask – 10 ml hard water + 5ml buffer solution (pH 10)\n"
         "3) Indicator - 3-4 drops of Eriochrome black T\n"
         "4) End point – Wine red to sky blue")
st.subheader("Observation Table:-")
import streamlit as st

def main():
    st.title("Observation Table")

    # Get user input for the number of observations
    num_observations = st.number_input("Enter the number of observations:", min_value=1, step=1)

    # Create a table
    table = [["Sr. No.", "IBR (ml)", "FBR (ml)", "Diff. in Reading (ml)", "Constant Burette Reading (ml)"]]

    # Populate the table with user input
    for i in range(1, num_observations + 1):
        sr_no = i
        ibr = st.number_input(f"{i}. IBR (ml):", min_value=0.0, step=0.1)
        fbr = st.number_input(f"{i}. FBR (ml):", min_value=0.0, step=0.1)
        diff_reading = fbr - ibr
        constant_burette_reading = st.number_input(f"{i}. Constant Burette Reading (ml):", min_value=0.0, step=0.1)

        # Add a row to the table
        table.append([sr_no, ibr, fbr, diff_reading, constant_burette_reading])

    # Display the table
    st.table(table)

if __name__ == "__main__":
    main()


# Given molarity of Na2-EDTA solution
st.header("Calculations:-")
st.subheader("(I) Estimation of total hardness:")
st.write("(Given molarity of Na2-EDTA solution = 0.01M)")
st.write("1000ml 1 M EDTA = 1 mole of CaCO3= 100 gm of CaCO3")
st.write("“X” ml M2 M EDTA = (X x M2 x 100)/1000")


import streamlit as st

def calculate_caco3(x, m2):
    result = (x * m2 * 100) / 1000
    return result

def main():
    st.write("EDTA Calculator")

    # Input fields
    x = st.number_input("Enter the volume in ml:")
    m2 = st.number_input("Enter the molarity:")

    if st.button("Calculate"):
        # Calculate CaCO3
        caco3_result = calculate_caco3(x, m2)

        # Display the result
        st.write(f"X ml M2 M EDTA = ({x} x {m2} x 100)/1000")
        st.write(f"The value of CaCO3 is {caco3_result:.2f} gm")
        st.write(f"If 10 ml of hard water sample contains {caco3_result:.2f} gm of CaCO3")
        st.write(f"1000 ml of hard water sample contains {caco3_result * 10:.2f} gm of CaCO3")
        st.write(f"mg of CaCO3 per litre hard water = {caco3_result:.2f} x 1000")
        st.header("Result:")
        st.write(f"Total hardness of water sample {caco3_result * 10:.2f} ppm")


if __name__ == "__main__":
    main()







st.header("Water Softening Methods")

import streamlit as st
from PIL import Image

# Open an image file
img_path = r"C:\Users\asu65\Downloads\attachments\Screenshot_20231114-100513_Drive.jpg"
img = Image.open(img_path)

# Display the image using Streamlit
st.image(img,  use_column_width=True)

import streamlit as st
from PIL import Image

# Open an image file
img_path = r"C:\Users\asu65\Downloads\attachments (1)\Screenshot_20231115-154457_Drive.jpg"
img = Image.open(img_path)

# Display the image using Streamlit
st.image(img,  use_column_width=True)

import streamlit as st
from PIL import Image

# Open an image file
img_path = r"C:\Users\asu65\Downloads\attachments (1)\Screenshot_20231115-154549_Drive.jpg"
img = Image.open(img_path)

# Display the image using Streamlit
st.image(img,  use_column_width=True)