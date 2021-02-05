rule _Vcasm_Protector_V1_X__vcasm_rqycta
{
	meta:
		description = "Vcasm Protector V1_X __ vcasm"
	strings:
		$a = {EB??5B5650726F746563745D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
