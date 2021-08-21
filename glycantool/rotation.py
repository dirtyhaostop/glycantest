import numpy as np

def rotation_mat_between_2vect(vector_orig, vector_fin):
    """Calculate the rotation matrix required to rotate from one vector to another.
    For the rotation of one vector to another, there are an infinit series of rotation matrices
    possible.  Due to axially symmetry, the rotation axis can be any vector lying in the symmetry
    plane between the two vectors.  Hence the axis-angle convention will be used to construct the
    matrix with the rotation axis defined as the cross product of the two vectors.  The rotation
    angle is the arccosine of the dot product of the two unit vectors.
    Given a unit vector parallel to the rotation axis, w = [x, y, z] and the rotation angle a,
    the rotation matrix R is::
              |  1 + (1-cos(a))*(x*x-1)   -z*sin(a)+(1-cos(a))*x*y   y*sin(a)+(1-cos(a))*x*z |
        R  =  |  z*sin(a)+(1-cos(a))*x*y   1 + (1-cos(a))*(y*y-1)   -x*sin(a)+(1-cos(a))*y*z |
              | -y*sin(a)+(1-cos(a))*x*z   x*sin(a)+(1-cos(a))*y*z   1 + (1-cos(a))*(z*z-1)  |
    @param vector_orig: The unrotated vector defined in the reference frame.
    @type vector_orig:  numpy array, len 3
    @param vector_fin:  The rotated vector defined in the reference frame.
    @type vector_fin:   numpy array, len 3
    """

    # Convert the vectors to unit vectors.
    vector_orig = vector_orig / np.linalg.norm(vector_orig)
    vector_fin = vector_fin / np.linalg.norm(vector_fin)

    # The rotation axis (normalised).
    axis = np.cross(vector_orig, vector_fin)
    axis_len = np.linalg.norm(axis)
    if axis_len != 0.0:
        axis = axis / axis_len

    # Alias the axis coordinates.
    x = axis[0]
    y = axis[1]
    z = axis[2]

    # The rotation angle.
    angle = np.arccos(np.dot(vector_orig, vector_fin))

    # Trig functions (only need to do this maths once!).
    ca = np.cos(angle)
    sa = np.sin(angle)

    # Initialize Rotation Matrix
    rot_mat = np.zeros((3, 3))

    # Calculate the rotation matrix elements.
    rot_mat[0, 0] = 1.0 + (1.0 - ca)*(x**2 - 1.0)
    rot_mat[0, 1] = -z*sa + (1.0 - ca)*x*y
    rot_mat[0, 2] = y*sa + (1.0 - ca)*x*z
    rot_mat[1, 0] = z*sa+(1.0 - ca)*x*y
    rot_mat[1, 1] = 1.0 + (1.0 - ca)*(y**2 - 1.0)
    rot_mat[1, 2] = -x*sa+(1.0 - ca)*y*z
    rot_mat[2, 0] = -y*sa+(1.0 - ca)*x*z
    rot_mat[2, 1] = x*sa+(1.0 - ca)*y*z
    rot_mat[2, 2] = 1.0 + (1.0 - ca)*(z**2 - 1.0)
    return rot_mat

def rotate_all_atoms_given_atomgroups(rot_mat, atomgroup):
    new_atomgroup = list()
    for atom in atomgroup:
        temp = np.zeros((3,1))
        temp[0,0] = atom.x
        temp[1,0] = atom.y
        temp[2,0] = atom.z
        temp = np.dot(rot_mat,temp)
        atom.x = temp[0,0]
        atom.y = temp[1,0]
        atom.z = temp[2,0]
        new_atomgroup.append(atom)
    return new_atomgroup

def get_rotation_matrix(angle, axis='x'):
    ca = np.cos(angle)
    sa = np.sin(angle)
    if axis == 'x':
        rot_mat = [[1, 0, 0],
                   [0, ca, -sa],
                   [0, sa, ca]]
    elif axis == 'y':
        rot_mat = [[ca, 0, sa],
                   [0, 1, 0],
                   [-sa, 0, ca]]
    else:
        rot_mat = [[ca, -sa, 0],
                   [sa, ca, 0],
                   [0, 0, 1]]
    return rot_mat