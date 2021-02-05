rule _Vcasm_Protector_1_0e__vcasm_jxgdai
{
	meta:
		description = "Vcasm_Protector 1_0e __ vcasm"
	strings:
		$a = {EB0A5B5650726F746563745D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
