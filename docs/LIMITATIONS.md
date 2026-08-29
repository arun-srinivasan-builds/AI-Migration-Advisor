# AI Migration Advisor — Limitations

## Purpose

AI Migration Advisor is an **educational and portfolio prototype** designed to explore how Generative AI can assist with preliminary enterprise data and analytics migration assessments.

The current version is **not a production migration assessment or architecture decision system**.

The following limitations were identified during development and testing.

---

## 1. Ungrounded LLM

The current application sends the migration scenario and structured prompt directly to a general-purpose LLM.

Current flow:

**User Scenario → Structured Prompt → LLM → Assessment**

The model is not currently connected to:

- Microsoft architecture documentation
- Migration best-practice documentation
- Organization-specific architecture standards
- Historical migration assessments
- Approved migration patterns
- Enterprise knowledge bases

Therefore, the generated assessment depends primarily on the knowledge and reasoning capability of the selected LLM.

### Impact

The model may generate an answer that sounds reasonable but is technically incomplete or incorrect.

---

## 2. Architectural Validation Is Not Guaranteed

The prompt instructs the model to identify inappropriate or unclear source-to-target migration scenarios.

However, testing demonstrated that prompt instructions alone cannot guarantee this behaviour.

### Example — Failed Test

The following scenario was deliberately tested:

**Azure HDInsight → Power BI**

The expected behaviour was for the model to question whether Power BI was an appropriate direct target for workloads running on HDInsight.

Instead, the model accepted the migration scenario and generated a complete assessment.

### Learning

> **Prompt engineering can guide LLM behaviour, but it cannot guarantee domain-grounded technical correctness.**

This was one of the most important findings from the prototype.

---

## 3. Smaller Local Model

The final prototype uses:

**qwen3:0.6b**

This model was selected because it provided better performance on the available local hardware.

A larger model, **qwen3:4b**, was also tested and produced better-quality responses, but local generation was considerably slower.

### Trade-off

**Smaller Model**
- Faster
- Lower hardware requirement
- Suitable for prototype development
- Lower reasoning capability

**Larger Model**
- Better response quality
- Higher hardware requirement
- Slower on the development machine

Therefore, some limitations in reasoning may be related to the capability of the selected lightweight model.

---

## 4. Prompt Constraints Do Not Guarantee Accuracy

The application prompt includes constraints instructing the model not to invent:

- Migration tools
- Timelines
- SLAs
- Costs
- Technical capabilities
- Information not supplied by the user

These constraints help guide the response.

However, LLMs are probabilistic systems and may still:

- Make assumptions
- Generate unsupported recommendations
- Miss architectural concerns
- Produce inaccurate technical statements

Prompt constraints therefore reduce risk but do not eliminate it.

---

## 5. Free-Text Input Can Be Ambiguous

The application deliberately allows users to describe migration scenarios freely rather than restricting them to predefined technologies or dropdown selections.

This provides flexibility but introduces another limitation.

Users may provide:

- Incomplete information
- Ambiguous technology names
- Incorrect terminology
- Conflicting requirements
- Invalid migration combinations

The current application does not perform deterministic validation of these inputs before sending them to the LLM.

---

## 6. No Enterprise Context

The prototype does not currently understand organization-specific information such as:

- Security policies
- Regulatory requirements
- Architecture standards
- Approved technology stacks
- Cost constraints
- Business SLAs
- Operational procedures
- Customer-specific dependencies

Therefore, recommendations remain generic unless the user explicitly provides this information.

---

## 7. No Automated Fact Validation

The application currently generates one LLM response and displays it to the user.

There is no secondary mechanism that independently verifies the generated technical recommendations.

For example, the application does not currently:

- Validate recommendations against trusted documentation
- Compare recommendations against approved architecture patterns
- Run deterministic migration compatibility rules
- Use a second validation model or agent
- Assign confidence scores to recommendations

---

## 8. Local Hardware Dependency

The prototype runs the LLM locally through Ollama.

Performance therefore depends heavily on the available computer hardware and selected model size.

During testing, the larger `qwen3:4b` model produced better responses but required approximately four minutes to generate a complete assessment on the development machine.

The lighter `qwen3:0.6b` model was therefore selected for the final prototype.

Different hardware may produce significantly different performance.

---

## 9. Not Designed for Production Scale

The current version is a single-user learning prototype.

It has not been designed or tested for:

- Multiple concurrent users
- High availability
- Enterprise authentication
- Authorization
- Audit logging
- Production monitoring
- Model observability
- Usage tracking
- Enterprise deployment
- Large-scale workload processing

---

## 10. Human Validation Is Required

The application intentionally displays a:

> **Human validation required**

message.

AI-generated assessments should be treated as preliminary guidance.

Final migration decisions should be reviewed by appropriate subject-matter experts, particularly for:

- Architecture
- Security
- Compatibility
- Performance
- Data governance
- Business continuity
- Cost
- Production migration planning

---

# Key Limitation

The most important limitation of the current prototype can be summarized as:

> **The application can generate a structured migration assessment, but it cannot currently guarantee that the assessment is technically correct or grounded in authoritative migration knowledge.**

---

# Potential Future Improvements

Future versions could explore:

- Retrieval-Augmented Generation (RAG)
- Trusted migration knowledge bases
- Microsoft architecture documentation grounding
- Platform compatibility validation
- Deterministic validation rules
- More capable LLMs
- Enterprise-approved cloud or private models
- Document ingestion
- Confidence indicators
- Multi-stage validation
- Agent-based assessment workflows
- Structured assessment reports

These improvements would be evaluated individually rather than automatically adding complexity to the prototype.

---

# Current Positioning

The current version should therefore be described as:

**AI-Assisted Preliminary Migration Assessment Prototype**

and not as:

**Automated Migration Architecture Decision Engine**

---

## Final Learning

One of the most valuable outcomes of this prototype was discovering its limitations through testing.

The failed architectural validation test demonstrated that building a working GenAI application is only the first step.

A reliable enterprise AI solution also requires:

**Domain Knowledge + Grounding + Validation + Testing + Human Judgement**
