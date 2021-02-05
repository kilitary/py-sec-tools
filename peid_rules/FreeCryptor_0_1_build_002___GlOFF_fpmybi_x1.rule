rule _FreeCryptor_0_1_build_002___GlOFF_fpmybi
{
	meta:
		description = "FreeCryptor 0_1 _build 002_ __ GlOFF"
	strings:
		$a = {8B0424409083C007803890907402EBFF906827????0064FF350000000064892500000000FFE4908B042464A3000000008B6424089083C408}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
