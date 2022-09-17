rule _TTProtect_V1_0X__somuch_nbsp__nbsp__Sign_By_fly__20080806_gawmfr
{
	meta:
		description = "TTProtect V1_0X __ somuch_nbsp_ _nbsp__ Sign_By_fly _ 20080806"
	strings:
		$a = {000000000000000000000000????????????????00000000000000000000000000000000000000004B65726E656C33322E646C6C00????????????????0000000000004C6F61644C6962726172794100000047657450726F6341646472657373005057539CE8??000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
