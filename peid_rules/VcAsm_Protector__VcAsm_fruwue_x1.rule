rule _VcAsm_Protector__VcAsm_fruwue
{
	meta:
		description = "VcAsm Protector __ VcAsm"
	strings:
		$a = {558BEC6AFF68????????68????????64A1000000005064892500000000E803000000C7840058EB01E983C00750C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
