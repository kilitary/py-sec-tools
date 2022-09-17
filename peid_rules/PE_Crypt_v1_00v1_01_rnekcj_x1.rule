rule _PE_Crypt_v1_00v1_01_rnekcj
{
	meta:
		description = "PE Crypt v1_00v1_01"
	strings:
		$a = {E8????????5B83EB05EB04524E44}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
