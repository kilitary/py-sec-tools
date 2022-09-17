rule _PE_Crypt32_Console_v1_0_v1_01_v1_02__nvcsgz
{
	meta:
		description = "PE Crypt32 _Console v1_0_ v1_01_ v1_02_"
	strings:
		$a = {E8000000005B83EB05EB04524E442185C07302F7}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
