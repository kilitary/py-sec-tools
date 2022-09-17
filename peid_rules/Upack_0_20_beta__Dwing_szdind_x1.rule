rule _Upack_0_20_beta__Dwing_szdind
{
	meta:
		description = "Upack 0_20 beta __ Dwing"
	strings:
		$a = {BE88014000AD8BF895A533C033C9AB48ABF7D8B104F3ABC1E00AB5??F3ABAD509751588D54855CFF16725A2C037302B0003C0772022C03500FB65FFFC1E3??B3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
