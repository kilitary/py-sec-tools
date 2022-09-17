rule _Exe_Shield_v1_7_qfbaur
{
	meta:
		description = "Exe Shield v1_7"
	strings:
		$a = {EB0668901F0600C39C60E80200000033C08BC483C004938BE38B5BFC81EB3F90}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
