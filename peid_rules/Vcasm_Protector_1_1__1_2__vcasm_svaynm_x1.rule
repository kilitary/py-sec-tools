rule _Vcasm_Protector_1_1__1_2__vcasm_svaynm
{
	meta:
		description = "Vcasm_Protector 1_1 _ 1_2 __ vcasm"
	strings:
		$a = {EB0B5B5650726F746563745D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
