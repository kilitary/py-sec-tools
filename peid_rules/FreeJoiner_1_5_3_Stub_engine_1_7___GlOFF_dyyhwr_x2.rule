rule _FreeJoiner_1_5_3_Stub_engine_1_7___GlOFF_dyyhwr
{
	meta:
		description = "FreeJoiner 1_5_3 _Stub engine 1_7_ __ GlOFF"
	strings:
		$a = {E833FDFFFF50E80D000000CCFF2508204000FF250C204000FF2510204000FF2514204000FF2518204000FF251C204000FF2520204000FF2524204000FF2528204000FF2500204000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
