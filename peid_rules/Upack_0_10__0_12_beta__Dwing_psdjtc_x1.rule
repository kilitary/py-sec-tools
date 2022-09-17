rule _Upack_0_10__0_12_beta__Dwing_psdjtc
{
	meta:
		description = "Upack 0_10 _ 0_12 beta __ Dwing"
	strings:
		$a = {BE48014000AD8BF895A533C033C9AB48ABF7D8B104F3ABC1E00AB5??F3ABAD509751AD87F5588D54865CFFD5725A2C037302B0003C0772022C03500FB65FFFC1}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
