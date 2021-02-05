rule _VcAsm_Protector_V1_0X__VcAsm_kndilf
{
	meta:
		description = "VcAsm Protector V1_0X__ VcAsm"
	strings:
		$a = {558BEC6AFF68????????68????????64A1000000005064892500000000E803000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
