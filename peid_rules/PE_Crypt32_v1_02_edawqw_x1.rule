rule _PE_Crypt32_v1_02_edawqw
{
	meta:
		description = "PE Crypt32 v1_02"
	strings:
		$a = {E8000000005B83????EB??524E4421}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
