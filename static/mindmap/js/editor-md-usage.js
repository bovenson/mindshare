/**
 * Created by bovenson on 17-7-10.
 */


function editorMdShow(elementId, markdown, tocContainer) {
    // console.log($("#" + elementId).find("textarea").val());
    var editorMdShowOptions = {
        markdown: markdown, // $("#" + elementId).find("textarea").val(),
        htmlDecode: "style,script,iframe",
        tocDropdown: true,
        toc: true,
        tocContainer: "#" + tocContainer,
        tocm: true,         // Using [TOCM]
        tex: true,                   // 开启科学公式TeX语言支持，默认关闭
        flowChart: true,             // 开启流程图支持，默认关闭
        // markdownSourceCode : true, // 是否保留 Markdown 源码，即是否删除保存源码的 Textarea 标签
        emoji           : true,
        taskList        : true,
        sequenceDiagram: true       // 开启时序/序列图支持，默认关闭,
    };
    // var mdEditor = editormd(elementId, editorMdShowOptions);
    // console.log(mdEditor.getHTML());
    var editorMdView = editormd.markdownToHTML(elementId, editorMdShowOptions);
}
