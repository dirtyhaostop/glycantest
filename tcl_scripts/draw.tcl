axes location Off
display projection Orthographic
color Display Background white

mol delrep 0 0

mol color ColorID 13
mol representation NewCartoon 0.300000 10.000000 4.100000 0
mol selection segid SUBA
mol material Opaque
mol addrep 0

mol color ColorID 13
mol representation CPK 1.000000 0.300000 12.000000 12.000000
mol selection segid SUBA and resid 50
mol material Opaque
mol addrep 0

mol color ColorID 20
mol representation CPK 1.000000 0.300000 12.000000 12.000000
mol selection segid M9XX
mol material Opaque
mol addrep 0

mol color ColorID 1
mol representation CPK 1.000000 0.300000 12.000000 12.000000
mol selection (segid SUBA and resid 50 and name ND2) or (segid M9XX and resid 2 and name C1)
mol material Opaque
mol addrep 0