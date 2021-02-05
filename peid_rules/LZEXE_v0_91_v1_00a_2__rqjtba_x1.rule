rule _LZEXE_v0_91_v1_00a_2__rqjtba
{
	meta:
		description = "LZEXE v0_91_ v1_00a _2_"
	strings:
		$a = {BF????0689F90E411F8CCB89FE}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
