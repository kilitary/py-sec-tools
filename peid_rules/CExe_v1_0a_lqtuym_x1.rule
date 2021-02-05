rule _CExe_v1_0a_lqtuym
{
	meta:
		description = "CExe v1_0a"
	strings:
		$a = {558BEC81EC0C02????56BE0401????8D85F8FEFFFF56506A??FF15541040??8A8DF8FEFFFF33D284C98D85F8FEFFFF7416}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
